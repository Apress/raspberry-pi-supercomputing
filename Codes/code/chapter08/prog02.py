from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
sys.stdout.write("My rank is: %d\n" % (comm.rank))

if comm.rank == 0:
    sys.stdout.write("Doing the task of Rank 0\n")

if comm.rank == 1:
    sys.stdout.write("Doing the task of Rank 1\n")
