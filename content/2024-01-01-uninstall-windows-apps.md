Title: Uninstalling Windows Apps that seem not to be installed
Date: 2024-01-01 14:00
Category: Windows
Tags: Windows

I found with [WizTree](https://diskanalyzer.com/) that there are some apps in
`C:\Program Files\WindowsApps` that seem not to be installed for my user, and
I'm the only user on my computer. Examples are games like Candy Crush and Disney
Magic Kingdoms. I found a solution to uninstall them in the [following
thread](https://answers.microsoft.com/en-us/windows/forum/all/unnecessary-apps-in-cprogram-fileswindowsapps/43f4552a-0445-4878-9ce3-8b7a4f45fe6a?page=2).

Basically, you have to start PowerShell as administrator and run the following
command:

```powershell

Get-AppxPackage -allusers  *disney* | Select Name, PackageFullName
Get-AppxPackage -allusers  *disney* | Remove-AppxPackage -allusers
```

The first command lists all apps that contain the string `disney` in their name.
The second command removes all apps that contain the string `disney` in their
name. You can also use `*candy*` to remove Candy Crush and so on.
