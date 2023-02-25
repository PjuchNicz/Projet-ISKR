from datetime import datetime
import datagouv
import file
import logging
import processing
def main():
    try :
        dataset_url = datagouv.get_last_url()
        file_path = file.download_file(dataset_url)
        file.unzip_file(file_path,"csv")

        processing.generate_rncp_rome()
        processing.save_dict_json(processing.generate_rncp_rome(), "rncp_rome")
    except Exception as e:
        print(f"Exit with error : {e}")
main()
