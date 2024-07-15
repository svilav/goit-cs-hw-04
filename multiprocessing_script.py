import time
from multiprocessing import Process, Queue


def search_keywords_in_file(file_path, keywords, q):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    q.put((keyword, file_path))
    except Exception as e:
        print(f"Error reading {file_path}: {e}")


def worker(file_paths, keywords, q):
    for file_path in file_paths:
        search_keywords_in_file(file_path, keywords, q)


def main_multiprocessing(file_list, keywords):
    start_time = time.time()
    num_processes = min(len(file_list), 4)  # визначимо кількість процесів

    chunk_size = len(file_list) // num_processes
    processes = []
    q = Queue()

    for i in range(num_processes):
        start_index = i * chunk_size
        end_index = None if i == num_processes - 1 else start_index + chunk_size
        process = Process(target=worker, args=(file_list[start_index:end_index], keywords, q))
        processes.append(process)
        process.start()

    results = {}
    for process in processes:
        process.join()

    while not q.empty():
        keyword, file_path = q.get()
        results.setdefault(keyword, []).append(file_path)

    end_time = time.time()
    print(f"Multiprocessing approach took {end_time - start_time:.2f} seconds")

    return results


if __name__ == "__main__":
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    keywords = ['error', 'warning', 'failed']
    results = main_multiprocessing(file_list, keywords)
    print(results)
