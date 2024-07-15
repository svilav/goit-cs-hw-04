import threading
import time


def search_keywords_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results.setdefault(keyword, []).append(file_path)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")


def worker(file_paths, keywords, results):
    for file_path in file_paths:
        search_keywords_in_file(file_path, keywords, results)


def main_threading(file_list, keywords):
    start_time = time.time()
    num_threads = min(len(file_list), 4)  # визначимо кількість потоків

    chunk_size = len(file_list) // num_threads
    threads = []
    results = {}

    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = None if i == num_threads - 1 else start_index + chunk_size
        thread = threading.Thread(target=worker, args=(file_list[start_index:end_index], keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Threading approach took {end_time - start_time:.2f} seconds")

    return results


if __name__ == "__main__":
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']
    keywords = ['error', 'warning', 'failed']
    results = main_threading(file_list, keywords)
    print(results)
