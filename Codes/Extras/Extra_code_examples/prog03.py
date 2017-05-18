from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
size = comm.Get_size()

if size == 5:
	sys.stdout.write("Success!\n")
else:
	sys.stdout.write("Error: This program must run with 5 processes!\n")
	comm.Abort()
