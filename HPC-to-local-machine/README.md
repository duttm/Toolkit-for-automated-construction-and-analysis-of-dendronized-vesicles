## Transfer files from HPC resources to local machine

Since the files on HPC resources add up to around 0.5-2 TB, we need scripts to simplify the transfer process. 

We follow these steps: 

1. Compress the parent folder in the HPC resource using a SLURM script. We have attached SLURM scripts for `TACC-Stampede2`, `SDSC-Expanse` and `PSC-Bridges2`. A compressed tar file is generated at the end of this step.

2. Pull the compressed file into local machine. Our local machine has security restrictions, and hence we have to "pull" the files from the HPC resource ( we can not "push" the files from HPC to local machine). Next, we open a `TMUX` terminal on our local machine and use this bash command: 

```
rsync -avzh username@HPC-resource:/path/to/tar/file /local/machine/target/directory
```

3. Once the tar file is transfered to the local machine, we unzip it using 

```
tar xvf <name of tar file>
```

Extra notes: 

If you want to selectively compress some files in the HPC-resource, you can use: 

```
find ./FOLDER -name "*.gro" -o -name "*.xtc" | tar -czvf FOLDER.tar.gz -T -
```
Here, gro and xtc files are selectively compressed in the tar file. This is very useful in decreasing the net size of the tar file. 
