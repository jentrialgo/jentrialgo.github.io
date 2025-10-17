title: The perfect strace command
date: 2025-10-17 12:00
category: Operating Systems, Debugging
tags: Operating Systems, Debugging

The Linux utility `strace` is essential for diagnosing process–kernel interactions, but its default output is often unusable. The key to effective debugging is using a specific set of flags that transform raw system call data into a structured, time‑stamped, and annotated log.

According to Avikam Rozenfeld in 
[this presentation](https://youtu.be/SUO0rQerpMk?t=726), here is the
essential command template, followed by a breakdown of why each flag is critical:

```
strace -f -s 256 -o trace.log -tt -T -y <your_command_here>
```

Flags and why they matter:

- **-f** — Follow children  
  Purpose: Trace child processes spawned by `fork`/`clone`.  
  Key benefit: Ensures you trace the entire application flow (e.g., piped commands).

- **-s 256** — Increase string size  
  Purpose: Increase the string output limit (default 32 bytes) to 256 bytes.  
  Key benefit: Prevents truncation of file paths and data being read or written.

- **-o <file>** — Output to file  
  Purpose: Redirect all `strace` output to a specified log file (e.g., `trace.log`).  
  Key benefit: Separates trace output from the program's standard output for easier analysis.

- **-tt** — Precise timestamp  
  Purpose: Prefix every line with the time of day including microsecond resolution.  
  Key benefit: Essential for observing the sequence of events across processes.

- **-T** — Time in syscall  
  Purpose: Show the time spent inside the kernel for each syscall.  
  Key benefit: Quickly spot bottlenecks (e.g., a long `poll` timeout).

- **-y** — File descriptor paths  
  Purpose: Translate file descriptor numbers into associated file paths, pipes, or socket addresses.  
  Key benefit: Eliminates manual lookup of fd → path associations.

## Power user flags (for complex scenarios)

- **-ff**  
  Use instead of `-f` together with `-o <prefix>`; writes each child's trace to its own file (e.g., `prefix.12345`), preventing interleaved logs.

- **-e <syscall_set>**  
  Filter output to specific system calls. Examples:  
  - `-e trace=file` — file operations  
  - `-e trace=open,poll,connect` — specific calls of interest  
  Key benefit: Drastically reduces log noise and focuses analysis.
