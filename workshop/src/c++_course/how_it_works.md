то же, что и c_course (workshop/how_it_works.md) , основано на risc checker 

# For subparser name list, use:

 python3 main.py --help


# init
python3 main.py oop_hard_task_1 --mode init --seed 12

# check correct solution 
python3 main.py oop_hard_task_1 --mode check --seed 12 --solution ../tests/cpp/integration/oop_hard_1_reference.cpp

# check incorrect solution 
python3 main.py oop_hard_task_1 --mode check --seed 12 --solution ../tests/cpp/integration/oop_hard_1_incorrect.cpp

# dry-run (prints generated tests)
python3 main.py oop_hard_task_1 --mode dry-run --seed 12
