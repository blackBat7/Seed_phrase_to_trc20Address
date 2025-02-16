from tronpy import Tron
from tronpy.providers import HTTPProvider
from multiprocessing import Pool, cpu_count
from tqdm import tqdm  # برای نمایش درصد پیشرفت

def seed_to_tron_address(seed_phrase):
    # ایجاد یک کیف پول ترون از عبارت seed
    client = Tron(HTTPProvider("https://api.trongrid.io"))
    wallet = client.generate_address_from_mnemonic(seed_phrase)
    return wallet['base58check_address']

def process_seed_phrase(seed_phrase):
    seed_phrase = seed_phrase.strip()
    if seed_phrase:
        try:
            tron_address = seed_to_tron_address(seed_phrase)
            result = f"Seed Phrase: {seed_phrase} -> Tron Address: {tron_address}\n"
            print(result)  # نمایش مراحل انجام در کنسول

            # ذخیره بلافاصله نتیجه در فایل
            with open('result.txt', 'a') as file:
                file.write(result)

            return result
        except Exception as e:
            error_message = f"Error converting seed phrase: {seed_phrase}. Error: {e}\n"
            print(error_message)  # نمایش خطا در کنسول

            # ذخیره بلافاصله خطا در فایل
            with open('tron_addresses.txt', 'a') as file:
                file.write(error_message)

            return error_message

def main():
    input_file = 'seed.txt'

    with open(input_file, 'r') as file:
        seed_phrases = file.readlines()

    with Pool(processes=cpu_count()) as pool:
        for _ in tqdm(pool.imap_unordered(process_seed_phrase, seed_phrases), total=len(seed_phrases)):
            pass

    print(f"Tron addresses have been saved to tron_addresses.txt")

if __name__ == "__main__":
    main()
