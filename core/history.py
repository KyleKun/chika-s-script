import os
import json


class History:
    @staticmethod
    def add_to_history(info, root_dir):
        """
        Add the downloaded episode to history
        :param info: "date": {"anime":  "", "episode":  "", "hour": "", "size":  "", "took":  ""}
        :param root_dir: root directory
        :return: None
        """
        try:
            with open(os.path.join(root_dir, 'data\\history.json'), 'r+', encoding='utf-8') as history:
                data = json.load(history)
                data["history"].append(info)
                history.seek(0)
                history.truncate(0)
                json.dump(data, history, ensure_ascii=False, indent=4)
            return True
        except Exception as e:
            print("Error parsing JSON history file: ", e)
            return False
        finally:
            history.close()

    @staticmethod
    def display_history(root_dir):
        try:
            with open(os.path.join(root_dir, 'data\\history.json'), 'r', encoding='utf-8') as history:
                data = json.load(history)

                # TODO print FANCY history
                for index, values in enumerate(data['history']):
                    print(index+1, ': ', values)

        except Exception as e:
            print("Error parsing JSON history file: ", e)
        finally:
            input('\nPress Enter to go back: ')
            history.close()
