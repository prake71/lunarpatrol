"""
Lunar Patrol - Choose The Lesser Of Two Evils

02/2017 by Peter Rake

Martin and Roger on their daily patrol around space station "Lunar 1".
Never knowing what could happen today. Sometimes meteroids, sometimes
space pirates, sometimes both. Due to limited resources on ammunition,
oxygen and fuel, they have always to take care how far they can go when
in struggle. In the worst case they have to decide between the lesser of
two evils: A col l iding maneuver with an enemy to drag at least this last
enemy still into death or staying alive in space avoiding any collision
until all resources on board are exhausted.
"""
import sys, os

def main():

    #figure out our directories
    global DATADIR, CODEDIR
    localpath = os.path.split(os.path.abspath(sys.argv[0]))[0]
    testdata = localpath
    testcode = os.path.join(localpath, 'code')
    if os.path.isdir(os.path.join(testdata, 'data')):
        DATADIR = testdata
    if os.path.isdir(testcode):
        CODEDIR = testcode

    #apply our directories and test environment
    os.chdir(DATADIR)
    sys.path.insert(0, CODEDIR)

    try:
        import game

    except ImportError:
        pass

        # run game and protect from exceptions
    try:
        import main, pygame
        main.main(sys.argv)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (Control-C)...")

# call the main function, start up my_game
if __name__ == "__main__":
    main()


    

    
