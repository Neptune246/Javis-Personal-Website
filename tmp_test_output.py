from pathlib import Path
p = Path('temp_test_stdout.txt')
p.write_text('hello world\n', encoding='utf-8')
print('SCRIPT_DONE')
