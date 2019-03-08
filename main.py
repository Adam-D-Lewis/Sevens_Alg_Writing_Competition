#!/usr/bin/env python3

from single_game import single_game
import matplotlib.pyplot as plt
from time import time
import configparser

def run_single_game():
    return single_game()

run_in_parallel = 1

# print(sys.argv[0])

if __name__ == "__main__":
    num_games = 1000

    #read win tally
    config = configparser.ConfigParser()
    try:
        config.read('win_tally.txt')
        total_wins = float(config['WIN_TALLY']['total_wins'])
        total_games_played = float(config['WIN_TALLY']['total_games_played'])
        latest_win_percentage = float(config['WIN_TALLY']['latest_win_percentage'])
    except:
        config['WIN_TALLY'] = {'total_wins': '0',
                               'total_games_played': '0',
                               'latest_win_percentage': '0'}
        total_wins = float(config['WIN_TALLY']['total_wins'])
        total_games_played = float(config['WIN_TALLY']['total_games_played'])
        latest_win_percentage = float(config['WIN_TALLY']['latest_win_percentage'])

    total_wins = float(config['WIN_TALLY']['total_wins'])
    total_games_played = float(config['WIN_TALLY']['total_games_played'])
    latest_win_percentage = float(config['WIN_TALLY']['latest_win_percentage'])

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
    for i, val in enumerate(results):
        hwp.append((hwp[-1]*i + val)/(i+1))
    print('hwp' + str(num_games) + ' = ' + str(round(hwp[-1]*100, 1)))


    plt.figure()
    plot_start_index = 100
    plt.plot(range(plot_start_index, len(hwp)), hwp[plot_start_index:])
    plt.xlabel('number of games')
    plt.ylabel('win fraction')
    plt.title('Win Fraction vs. Game Number')
    # plt.show()

    #write to file to continue tally
    config['WIN_TALLY']['penultimate_win_percentage'] = str(latest_win_percentage)
    total_wins = total_wins+sum(results)
    total_games_played = total_games_played+len(results)
    latest_win_percentage = total_wins/total_games_played
    config['WIN_TALLY']['total_wins'] = str(total_wins)
    config['WIN_TALLY']['total_games_played'] = str(total_games_played)
    config['WIN_TALLY']['latest_win_percentage'] = str(latest_win_percentage)

    with open('win_tally.txt', 'w') as f:
        config.write(f)
    print('bye')