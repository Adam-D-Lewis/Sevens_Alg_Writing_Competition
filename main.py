from single_game import single_game
import matplotlib.pyplot as plt
from time import time
'''main.py
load results

for i in range(num_matches):
    single_game(results)

save results

results that I want to record include the number of games and the win percentage with the human strategy
'''

def run_single_game():
    return single_game()

run_in_parallel = 1

if __name__ == "__main__":
    num_games = 5000

    if run_in_parallel:
        from joblib import Parallel, delayed
        import multiprocessing
        #---------------------------------Parallel Code --------------------------------
        num_cores = multiprocessing.cpu_count()

        t0 = time()
        results = Parallel(n_jobs=num_cores)(delayed(run_single_game)() for i in range(num_games))
        t1 = time()
    else:
        #------------------Nonparallel Code (Serial)-------------------------------------
        results = []
        t0 = time()
        for i in range(num_games):
            results.append(single_game())
        t1 = time()
    #--------------------------------------------------------------------------------
    dt = t1 - t0
    print('dt = ' + str(dt))

    # update the human win percentage(hwp)
    hwp = [0]
    N = 0
    for val in results:
        hwp.append((hwp[-1]*N + val)/(N+1))
        N = N + 1
    print('hwp' + str(num_games) + ' = ' + str(round(hwp[-1]*100, 1)))


    plt.figure()
    plt.plot(hwp[1:])
    plt.xlabel('number of games')
    plt.ylabel('win fraction')
    plt.show()

    print('bye')