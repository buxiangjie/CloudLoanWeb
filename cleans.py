import os
import shutil


def cleans():
	os.system("allure generate --clean ./results -o ./report")
	if os.path.exists("./results"):
		shutil.rmtree("./results")
	if os.path.exists("./screenshot"):
		shutil.rmtree("./screenshot")


if __name__ == '__main__':
	cleans()
