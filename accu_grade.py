import os 
import subprocess
import glob

def main():
    students = os.listdir("Project3")
    src_files_dir = os.path.abspath("eecs280x-project3")
    end_dir = os.path.abspath(".")
    cfiles = glob.glob(os.path.join(src_files_dir, "*.c"))
    
    out_content = ""
    pass_content = ""

    os.chdir("Project3")
    student = "afwilkin"
    for student in students:
        print(student)
        os.chdir(student)
        try:
            cmd = ["gcc", "-I", src_files_dir, "-std=gnu99", "-g", "-Wall",
                   "-O4", "-o", "student_code",  "digitclass.c", "list.c"] 
            cmd += cfiles 
            
            subprocess.check_call(cmd) 
            
            results = []
            passs = []
            for dec_val in [25, 50, 100]:
               try:
       #            print(os.listdir("."))
                   ex_cmd = ["./student_code", "-d", str(dec_val)]
                   #subprocess.check_call(ex_cmd)
                   output = subprocess.check_output(ex_cmd)
        #           print(output[-3])
                   results.append(output.split("\n")[-2])
         #          print(results)
                   passs.append(str(output.split("\n")[-2] > 80))
                   out_content += "{}:{}\n".format(student, " ".join(results))
                   pass_content += "{}:{}\n".format(student, " ".join(passs))
               except subprocess.CalledProcessError:
                   results.append("FAIL")
                   

        except subprocess.CalledProcessError:
            out_content += str(student) + " did not submit\n"  
            pass

        finally:
            os.chdir("../")
    
    os.chdir(end_dir)
    print(os.listdir("."))
            
    with open("student_results.txt", "w") as f:
    #    os.chdir(end_dir)    
        f.write(out_content)

    with open("student_pass.txt", "w") as fi:
    #    os.chdir(end_dir)    
        fi.write(pass_content)
        


if __name__ == "__main__":
    main()



