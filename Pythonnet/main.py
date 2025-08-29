from pythonnet import load
load("coreclr")
import clr
clr.AddReference("System")

from System import Console
Console.WriteLine("Hello World with pythonnet, using Console.WriteLine.")
