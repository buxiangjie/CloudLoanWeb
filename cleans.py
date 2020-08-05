import os
import shutil

if os.path.exists("./report"):
	shutil.rmtree("./report")
if os.path.exists("./screenshot"):
	shutil.rmtree("./screenshot")
if os.path.exists("./results"):
	shutil.rmtree("./results")