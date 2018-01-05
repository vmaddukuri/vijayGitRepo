from subprocess import check_output

op = check_output(['python', 'psoops1.py'])
print(op.decode('ascii'))