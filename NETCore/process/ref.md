# External process/command 

## .NET built-in method 

- namespace : System.Diagnostics.Process

```
  string command = "ls -la";
  string result = "";
  using (System.Diagnostics.Process proc = new System.Diagnostics.Process())
  {
      proc.StartInfo.FileName = "/bin/bash";
      proc.StartInfo.Arguments = "-c \" " + command + " \"";
      proc.StartInfo.UseShellExecute = false;
      proc.StartInfo.RedirectStandardOutput = true;
      proc.StartInfo.RedirectStandardError = true;
      proc.Start();

      result += proc.StandardOutput.ReadToEnd();
      result += proc.StandardError.ReadToEnd();

      proc.WaitForExit();
  }

```

## External Package (Renci.SshNet)

- namespace : 
  - using Renci.SshNet;
  - using Renci.SshNet.Sftp;

```
    string host = "172.16.1.130";
    string username = "root";
    string password = @"Admin!23";

    string remoteDirectory = "/etc";
    
    using (SftpClient sftp = new SftpClient(host, username, password))
    {
        
        try
        {
            sftp.Connect();

            var files = sftp.ListDirectory(remoteDirectory);

            foreach (var file in files)
            {
                Console.WriteLine(file.Name);
            }

            sftp.Disconnect();
        }
        catch (Exception e)
        {
            Console.WriteLine("An exception has been caught " + e.ToString());
        }
    }

```

> Ref : https://ourcodeworld.com/articles/read/369/how-to-access-a-sftp-server-using-ssh-net-sync-and-async-with-c-in-winforms