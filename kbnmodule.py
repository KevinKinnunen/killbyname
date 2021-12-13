import psutil 
import argparse
import time
import getpass

class Methods:
    def CloseProcessName(name):
        for proc in psutil.process_iter():
            if name in proc.name():
                pid = proc.pid
                p = psutil.Process(pid)
                p.terminate()
                time.sleep(2.5)
                quit()
                return CloseProcessName

    def CloseProcessPid(procid):
        for proc in psutil.process_iter():
            if procid == proc.pid:
                pid = proc.pid
                p = psutil.Process(pid)
                p.terminate()
                time.sleep(2.5)
                quit()
                return CloseProcessPid

    def GetProcessInfo(pinfo):
        process_infos = list()
        for proc in psutil.process_iter():
            if pinfo in proc.name():
                proc_info = dict()
                with proc.oneshot():
                    proc_info["User"] = getpass.getuser()
                    proc_info["name"] = proc.name()
                    proc_info["pid"] = proc.pid
                    proc_info["cpu_percent"] = proc.cpu_percent()
                    proc_info["exe"] = proc.exe()

                    mem_info = proc.memory_info()
                    proc_info["mem_rss"] = mem_info.rss
                    proc_info["num_threads"] = proc.num_threads()
                    proc_info["nice_priority"] = proc.nice()
                    process_infos.append(proc_info)
                return process_infos

