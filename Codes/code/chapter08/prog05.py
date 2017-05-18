from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size
name = MPI.Get_processor_name()

shared = (rank+1)*(rank+1)

comm.send(shared, dest=(rank+1) % size)
data = comm.recv(source=(rank-1) % size)

sys.stdout.write("Name: %s\n" % name)
sys.stdout.write("Rank: %d\n" % rank)
sys.stdout.write("Data %d came from rank: %d\n" % (data, (rank-1) % size))
