from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

sys.stdout.write("Rank: %d," % rank)
sys.stdout.write(" Process Count: %d\n" % size)
