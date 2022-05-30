import os
from colorama import Fore, init
import runner

init(autoreset=True)

progover = False


def red(text):
	return Fore.RED + text + Fore.RESET

class Lexer:
	def __init__(self, line: str, filename: str):
		if ">" not in line:
			print(red(f"SyntaxError: '{line}' does not contain '>'"))
			quit()	

		self.filename = filename
		self.line = line
		self.cmd = line.split(">", 1)[0].rstrip()	

		try:
			self.args = line.split(">", 1)[1].strip()
			self.run()

		except IndexError:
			return

	def run(self):
		indchars = len(self.cmd) - len(self.cmd.lstrip(" "))
		ind = " " * indchars
		if self.cmd.strip() == "say":
			runner.code += (ind + "print(" + self.args + ")\n")

		elif self.cmd.strip() == "var" or self.cmd.strip() == "array":
			if "+=" in self.args:
				name, defin = self.args.split("+=", 1)[0].strip(), self.args.split("+=", 1)[1].strip()

			elif "-=" in self.args:
				name, defin = self.args.split("-=", 1)[0].strip(), self.args.split("-=", 1)[1].strip()

			elif "*=" in self.args:
				name, defin = self.args.split("*=", 1)[0].strip(), self.args.split("*=", 1)[1].strip()

			elif "/=" in self.args:
				name, defin = self.args.split("/=", 1)[0].strip(), self.args.split("/=", 1)[1].strip()

			elif "%=" in self.args:
				name, defin = self.args.split("%=", 1)[0].strip(), self.args.split("%=", 1)[1].strip()

			else:
				name, defin = self.args.split("=", 1)[0].strip(), self.args.split("=", 1)[1].strip()

			if defin == "[]":
				print(red(f"LF: compiler error: array cannot be empty"))
				quit()

			else:
				runner.code += (ind + self.args + "\n")

		elif self.cmd.strip() == "string":
				if "+=" in self.args:
					name, defin = self.args.split("+=", 1)[0].strip(), self.args.split("+=", 1)[1].strip()

				elif "-=" in self.args:
					name, defin = self.args.split("-=", 1)[0].strip(), self.args.split("-=", 1)[1].strip()

				elif "*=" in self.args:
					name, defin = self.args.split("*=", 1)[0].strip(), self.args.split("*=", 1)[1].strip()

				elif "/=" in self.args:
					name, defin = self.args.split("/=", 1)[0].strip(), self.args.split("/=", 1)[1].strip()

				elif "%=" in self.args:
					name, defin = self.args.split("%=", 1)[0].strip(), self.args.split("%=", 1)[1].strip()

				else:
					name, defin = self.args.split("=", 1)[0].strip(), self.args.split("=", 1)[1].strip()

				runner.code += (ind + name + ": str " + f" = str({defin})" + "\n")

		elif self.cmd.strip() == "interger":
				if "+=" in self.args:
					name, defin = self.args.split("+=", 1)[0].strip(), self.args.split("+=", 1)[1].strip()

				elif "-=" in self.args:
					name, defin = self.args.split("-=", 1)[0].strip(), self.args.split("-=", 1)[1].strip()

				elif "*=" in self.args:
					name, defin = self.args.split("*=", 1)[0].strip(), self.args.split("*=", 1)[1].strip()

				elif "/=" in self.args:
					name, defin = self.args.split("/=", 1)[0].strip(), self.args.split("/=", 1)[1].strip()

				elif "%=" in self.args:
					name, defin = self.args.split("%=", 1)[0].strip(), self.args.split("%=", 1)[1].strip()

				else:
					name, defin = self.args.split("=", 1)[0].strip(), self.args.split("=", 1)[1].strip()

				runner.code += (ind + name + ": int " + f" = int({defin})" + "\n")

		elif self.cmd.strip() == "float":
				if "+=" in self.args:
					name, defin = self.args.split("+=", 1)[0].strip(), self.args.split("+=", 1)[1].strip()

				elif "-=" in self.args:
					name, defin = self.args.split("-=", 1)[0].strip(), self.args.split("-=", 1)[1].strip()

				elif "*=" in self.args:
					name, defin = self.args.split("*=", 1)[0].strip(), self.args.split("*=", 1)[1].strip()

				elif "/=" in self.args:
					name, defin = self.args.split("/=", 1)[0].strip(), self.args.split("/=", 1)[1].strip()

				elif "%=" in self.args:
					name, defin = self.args.split("%=", 1)[0].strip(), self.args.split("%=", 1)[1].strip()

				else:
					name, defin = self.args.split("=", 1)[0].strip(), self.args.split("=", 1)[1].strip()

				runner.code += (ind + name + ": float " + f" = float({defin})" + "\n") 

		elif self.cmd.strip() == "bool":
				name, defin = self.args.split("=", 1)[0].strip(), self.args.split("=", 1)[1].strip()
				if defin not in ["True", "False"]:
					print(red(f"LF: compiler error: '{defin}' cannot be a parsed as 'bool'"))
					quit()

				runner.code += (ind + name + f" = {defin}" + "\n")

		elif self.cmd.strip() == "attr" or self.cmd.strip() == "attribute":
				runner.code += (ind + "self." + self.args + "\n") 

		elif self.cmd.strip() == "func":
				runner.code += (ind + "@jit(fastmath=True, parallel=True)\n")
				runner.code += (ind + "def " + self.args[:-1] + ":\n") 

		elif self.cmd.strip() == "lightfunc":
				runner.code += (ind + "@jit(nopython=True, fastmath=True, parallel=True)\n")
				runner.code += (ind + "def " + self.args[:-1] + ":\n")

		elif self.cmd.strip() == "method":
				if "this" in self.args:
					self.args = self.args.replace("this", "self")

				if "__Start__" in self.args:
					self.args = self.args.replace("__Start__", "__init__")

				runner.code += (ind + "def " + self.args[:-1] + ":\n") 

		elif self.cmd.strip() == "constmethod":
				name, args = self.args[:-1].strip().split("(")[0], self.args[:-1].strip().split("(")[1].rstrip(")")

				if args != "":
					print(red(f"LF: compiler error: '{name}' cannot be a constmethod because it takes args"))
					quit()

				runner.code += (ind + "def " + name + "()" ":\n") 

		elif self.cmd.strip() == "class":
				runner.code += (ind + "class " + self.args[:-1] + ":\n") 

		elif self.cmd.strip() == "call":
				runner.code += (ind + self.args + "\n") 

		elif self.cmd.strip() == "if":
				runner.code += (ind + "if " + self.args[:-1].replace("||", "or").replace("&&", "and") + ":\n") 

		elif self.cmd.strip() == "elif":
				runner.code += (ind + "elif " + self.args[:-1].replace("||", "or").replace("&&", "and") + ":\n") 

		elif self.cmd.strip() == "else":
				runner.code += (ind + "else:\n")

		elif self.cmd.strip() == "unless":
				runner.code += (ind + "if not " + self.args[:-1].replace("||", "or").replace("&&", "and") + ":\n")

		elif self.cmd.strip() == "while":
				runner.code += (ind + "while " + self.args[:-1].replace("||", "or").replace("&&", "and") + ":\n")

		elif self.cmd.strip() == "for":
				runner.code += (ind + "for " + self.args[:-1].replace("||", "or").replace("&&", "and").replace("interger.Range(", "range(") + ":\n")

		elif self.cmd.strip() == "break":
				runner.code += (ind + "break\n")

		elif self.cmd.strip() == "continue":
				runner.code += (ind + "continue\n")

		elif self.cmd.strip() == "pass":
				runner.code += (ind + "pass\n")

		elif self.cmd.strip() == "return":
				runner.code += (ind + "return " + self.args + "\n")

		elif self.cmd.strip() == "try":
				runner.code += (ind + "try:\n")

		elif self.cmd.strip() == "catch":
				runner.code += (ind + f"except {self.args[:-1]}:\n")

		elif self.cmd.strip() == "throw":
				runner.code += (ind + f"raise {self.args[:-1]}:\n")

		elif self.cmd.strip() == "finally":
				runner.code += (ind + f"finally:\n")

		elif self.cmd.strip() == "force":
				runner.code += (ind + f"assert {self.args}\n")

		elif self.cmd.strip() == "global":
				runner.code += (ind + f"global {self.args}\n")

		elif self.cmd.strip() == "del":
				runner.code += (ind + f"del {self.args}\n")

		elif self.cmd.strip() == "undefined":
				runner.code += (ind + self.args + "\n")

		elif self.cmd.strip() == "with":
				runner.code += (ind + f"with {self.args[:-1]}:\n")

		elif self.cmd.strip() == "use":

				if self.args == "time.lf":
					runner.code += (ind + f"import time as pytime\n")

				elif self.args == "ui.lf":
					runner.code += (ind + f"import tkinter as pytk\n")

				elif self.args == "os.lf":
					runner.code += (ind + f"import os as pyos\n")
					runner.code += (ind + f"import platform as pyplat\n")

				elif self.args == "math.lf":
					runner.code += (ind + f"import math as pymaths\n")

				elif self.args == "random.lf":
					runner.code += (ind + f"import random as pyrand\n")
					runner.code += (ind + f"import string as pystr\n")

				elif self.args == "system.lf":
					runner.code += (ind + f"import sys as pysys\n")

				elif self.args == "decimal.lf":
					runner.code += (ind + f"import decimal as pydec\n")
				
				try:
					with open("c:\\LF\\builtins\\" + self.args, "r") as f:
						for i in f.readlines():
							Lexer(i.replace("\n", "").replace("\t", "    ").split("#", 1)[0], self.filename) if i.split("#", 1)[0].isspace() == False and i.startswith("#") == False else None

				except FileNotFoundError:

					try:
						with open("c:\\LF\\modules\\" + self.args, "r") as f:
							for i in f.readlines():
								Lexer(i.replace("\n", "").replace("\t", "    ").split("#", 1)[0], self.filename) if i.split("#", 1)[0].isspace() == False and i.startswith("#") == False else None

					except FileNotFoundError:

						try:
							with open(self.args, "r") as f:
								for i in f.readlines():
									Lexer(i.replace("\n", "").replace("\t", "    ").split("#", 1)[0], self.filename) if i.split("#", 1)[0].isspace() == False and i.startswith("#") == False else None

						except FileNotFoundError:
							print(red(f"ModuleError: '{self.args}' could not be found in 'builtins', 'modules', or the current directory. Perhaps you missed the .lf at the end?"))
							exit()

		else:
				try:
					runner.code += (ind + f"{self.cmd.strip()}()\n")

				except NameError:
					print(red(f"LF: compiler error: '{self.cmd.strip()}' is not a valid keyword in this context"))
					quit()