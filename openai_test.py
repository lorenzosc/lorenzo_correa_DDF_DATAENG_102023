import openai
import csv
import json
import traceback
import time
import asyncio
from config import openai_key

async def get_gpt_response (
    product_description: str, semaphore: asyncio.Semaphore, 
    product_name: str, retry: int = 3
) -> dict:
    """Get chat completion from chat gpt for given message

    :param product_description: description for prompt in chatgpt
    :param semaphore: Semaphore used for control of tasks
    :param product_name: Product name for inclusion in response
    :param retry: number of retries to get response before giving up
    :return: dictionary of gpt response
    """
    for j in range(retry):
        try:
            message = f"What product_category, material, and features would you give to this product? " +\
            f"give me the response as json, and features a dictionary in that json." +\
            f"\nProduct is:\n{product_description}" 
            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=[{"role": "user", "content":message}])
            reply = completion["choices"][0]["message"]["content"]
            print(reply)

            #find json within the reply
            start = reply.find("{")
            end = len(reply) - reply[::-1].find("}")

            reply_dict = json.loads(reply[start:end])
            reply_dict["product_name"] = product_name
            semaphore.release()
            return reply_dict
        
        except Exception:
            traceback.print_exc()
            time.sleep(30)

    semaphore.release()
    raise Exception("Couldn't get ChatGPT response")


def record_results (
    output_path: str, last_line_path: str, 
    last_line: int, output_data: list[dict]
) -> None:
    """Record returned results

    :param output_path: Path to save output
    :param last_line_path: Path to record the last line returned
    :param last_line: Number of the last line returned
    :param output_data: Output data to record 
    """
    with open(last_line_path, "w+") as file:
        file.write(str(last_line))

    with open(output_path, "r+") as file:
        
        #load previous extracted data
        file_data = json.load(file)

        #append answers from chatgpt
        for product in output_data:
            if isinstance(product, dict):
                file_data["products"].append(product)
        
        #reset pointer just for precaution
        file.seek(0)

        #add data to json file
        json.dump(file_data, file, indent=4)

async def async_extract (
    file_reader: csv.reader, skip_lines: int = 0, 
    semaphore_value: int = 1, limit: int = 1000
) -> tuple[int, list[dict]]:
    """Asynchronous function for asynchronous requests in chatgpt

    :param file_reader: csv file reader (iterable)
    :param skip_lines: lines from start of the file to skip
    :param semaphore_value: how many tasks can be done at once
    :param limit: how many lines can be read with one execution
    :return: last line read and list of responses
    """
    products = []
    sem = asyncio.Semaphore(semaphore_value)
    tasks = {}
    try:
        for i, line in enumerate(file_reader):

            if i < skip_lines:
                continue

            last_line = i
            print(f"{i}")

            await sem.acquire()
            task = asyncio.create_task(get_gpt_response(line[2], sem, line[1]))
            tasks[i] = task
            
            limit -= 1
            if not limit:
                last_line = i+1
                break
    except KeyboardInterrupt:
        pass

    finally:
        for product in asyncio.as_completed(tasks.values()):

            try:
                result = await product
                products.append(result)

            except Exception:
                traceback.print_exc()

        return last_line, products

async def main () -> None:
    openai.api_key = openai_key
    file_path = r"C:\Users\loren\Desktop\PC\Dadosfera\corpus_0.csv"
    last_line_path = r"C:\Users\loren\Desktop\last_line.txt"
    output_path = r"C:\Users\loren\Desktop\products.json"

    #reads file with information over the last iteration
    try:
        with open(last_line_path, 'r') as file:
            for line in file.readlines():
                last_line = int(line)
    except:
        last_line = 0

    with open(file_path, newline='') as csvfile:

        reader = csv.reader(csvfile)
        #skip header
        next(reader, None)

        try:
            last_line, products = await async_extract(reader, skip_lines=last_line, semaphore_value=3)

        except Exception as e:
            traceback.print_exc()
            
        finally:
            record_results(output_path, last_line_path, last_line, products)

if __name__ == '__main__':
    time_start = time.time()
    asyncio.run(main())
    time_end = time.time()
    print(f"{time_end-time_start}")