# Main youtube tutorial scripts

## Introduction text

Welcome to this series of tutorials on how to use Jupyter notebooks for analyzing annotation results!

If you're working in the field of biology or bioinformatics, probably you know that analyzing this kind of data can be a challenging task. 
So that's why we've created a set of Jupyter notebooks that can help you streamline the analysis process and generate meaningful insights from your annotation results.

These notebooks are a set of tools designed to assist the researcher in the analysis of annotation results obtained from homology searches of protein databases. 
All these notebooks are built using Python and popular data analysis libraries like Pandas, Matplotlib, and Seaborn. Each notebook is focused on a specific task, 
but all can be used to analyze and interpret homology search results.

By using our Jupyter notebooks, you can save a lot of time and effort that would otherwise be spent on manual data processing and analysis. 
You can also customize the notebooks to fit your specific needs, by modifying the code and adding new functionality.

So, whether you're a biologist, a bioinformatician, or anyone interested in analyzing annotation data, 
our Jupyter notebooks are a great tool to have in your toolkit. We hope you find the tutorials helpful, and we encourage you to try our notebooks 
and provide us feedback and suggestions for improvement. 

I will leave the GitHub link in the description, and in the upcoming tutroial I'll explain step-by-step how to use these amazing tools.

Thanks for watching!

*3 min*

## Docker Installation Process
### [Section 1: Introduction]
**Host (You)**: "Hello everyone, and welcome back to my channel! Today, we're going to walk through the installation process for BioswiftAnalytics, a comprehensive package that includes several Jupyter notebooks designed to simplify and streamline the analysis of biological data, and so a useful bioinformatics tool that helps researchers analyze biological data using Python and Jupyter notebooks. So, let’s get started!"

### [Section 2: Docker Installation]
**Host**: "In the github page of the project, you will find all information about the installation process in the "quickstart" section. First of all, we need to have Docker installed on our computer. Docker is a fantastic platform that lets us package applications and their dependencies into containers. These containers can run on any system that has Docker installed, ensuring everything works perfectly without any compatibility issues."

**[Cut to Screen Recording: Docker Website]**

**Host**: "If you haven't installed Docker yet, no worries. Head over to [docker.com](https://www.docker.com) and follow the installation instructions for your operating system. It’s a pretty straightforward process and the website provides all the guidance you need."

### [Section 3: Pulling the Docker Image]
**Host**: "Once Docker is up and running, it’s time to download the BioswiftAnalytics Docker image. Open your terminal or command prompt and type the following command:"

**[Cut to Screen Recording: Terminal]**
**[On-Screen Text]**
```bash
docker pull lorenzoarcioni/bioswiftanalytics
```

**Host**: "This command tells Docker to pull the BioswiftAnalytics image from the Docker repository. Depending on your internet speed, this might take a few minutes, so feel free to grab a cup of coffee while you wait."

### [Section 4: Setting Up Directories]

**Host**: "Let’s now set up a couple of directories on your local machine. These directories will help us link the container's filesystem with our local filesystem, making it easy to transfer data in and out of the container."

**[Cut to Screen Recording: Terminal]**
**[On-Screen Text]**
```bash
mkdir data
mkdir results
```

**Host**: "What we’re doing here is creating two directories named 'data' and 'results'. The 'data' directory will hold the input files for our analyses, and the 'results' directory will store the output files, such as graphs and tables."

In this case, we use the test files by downloading the TAR archive from release section by running the following wget command. In this way, we have automatically set up our filesystem structure and files.

### [Section 5: Running the Docker Container]

**Host**: "Now that we have our directories set up and the Docker image downloaded, we can run the Docker container. This is where the magic happens! In your terminal, enter the following command:"

**[On-Screen Text]**
```bash
docker run -p 8888:8888 -v $(pwd)/results:/home/jupyter/results/ -v $(pwd)/data:/home/jupyter/data -d --name bioswiftanalytics lorenzoarcioni/bioswiftanalytics
```

**Host**: "This command run the docker container mapping the local filesystem directories to the container directories. In this way, the two directories are linked and perfectly synchronized. 



- `-p 8888:8888` maps port 8888 of the container to port 8888 on your local machine, so we can access Jupyter notebooks via our web browser.
- `-v $(pwd)/results:/home/jupyter/results/` links the local 'results' directory to the container’s '/home/jupyter/results/' directory.
- `-v $(pwd)/data:/home/jupyter/data` links the local 'data' directory to the container’s '/home/jupyter/data/' directory.
- `-d` runs the container in detached mode, meaning it runs in the background.
- `--name bioswiftanalytics` names the container 'bioswiftanalytics', which makes it easier to manage."

### [Section 6: Accessing Jupyter Notebooks]

**Host**: "With the container up and running, we can now access the Jupyter notebooks. Open your web browser and go to the address 127.0.0.1:8888. You should see the Jupyter interface, where you can start exploring the various notebooks included in BioswiftAnalytics."

**[Cut to Screen Recording: Browser]**

**Host**: "From here, you can upload your data to the 'data' directory within Jupyter, and any results you generate will be saved to the 'results' directory. This setup ensures a smooth workflow between your local machine and the Docker container."

### [Section 7: Managing Data]

**Host**: "Just to recap, the container has two main directories:

- The input data directory: `/home/jupyter/data/`
- The output data directory: `/home/jupyter/results/`

These directories are linked to your local 'data' and 'results' directories, respectively. So, you can easily transfer data for analysis by copying files into the local 'data' directory. The results will automatically appear in the local 'results' directory, making it very convenient to access and share your findings."

### [Section 8: Stopping and Removing the Container]

**Host**: "Once you’ve finished your analysis and no longer need the container running, you can stop and remove it to free up system resources. Use the following commands in your terminal:"

**[On-Screen Text]**
```bash
docker stop bioswiftanalytics && docker remove bioswiftanalytics
```

**Host**: "This command stops the running container and then removes it from your system. It’s always a good practice to clean up unused containers to keep your system tidy."

### [Section 9: Conclusion]

**Host**: "And that’s it! You’ve successfully installed and set up BioswiftAnalytics using Docker. Now you’re ready to dive into your bioinformatics analyses with a powerful set of tools at your disposal. If you found this tutorial helpful, please give it a thumbs up and subscribe to our channel for more tutorials like this. In the next tutorial, I'll show you how to use the first notebook of this series. So see you in the next video!"

*up to 10 mins*
## Jupyter notebook for Hit Rate Comparison (AnnoRate)

The process of analyzing hit percentages for sequences across diverse databases plays a pivotal role in bioinformatics research, because this evaluation method systematically assesses the performance of databases by quantifying the alignment success with sequences from an input transcriptome. The importance of this lies in its ability to guide researchers in selecting the most suitable database for their specific analysis. By providing a quantitative measure of database performance, the analysis enables researchers to optimize parameters, ensure quality control, and enhance resource efficiency. It facilitates data-driven decision-making, guiding researchers toward databases that align optimally with the biological data under investigation. In essence, the process contributes to the overall rigor and reliability of bioinformatics analyses, ensuring that computational resources are directed toward databases that yield accurate and biologically meaningful results. This abstract emphasizes the significance of hit percentage analysis in enhancing the quality and efficiency of bioinformatics research.

This notebook is a great tool for the hit percentages analysis of sequences across various databases.

*1 min*

## Jupyter notebook for Multi Database Annotation Summary (AnnoReport)

Have a comprehensive overview of all your alignment results, merge other statistic data with the result entries and map the matching sequences with online references, can greatly improve the clarity of your analysis process and give you an extra boost in the interpretation phase.

This notebook is capable of generating summary reports in XSLX or TSV format, consolidating the annotation results of a specific transcriptome obtained by running alignment software (Diamond or BLAST with both blastp/x tools) against various sequence databases. Additionally, this notebook can create links to the accession numbers for the input transcript sequences that mapped to the database, as well as resources on the NCBI and UniProt portals.

*1 min*

## Jupyter notebook for Enhanced Annotation Result Interpretation (AnnoViz)

Interpreting homology annotation results accurately and comprehensively is important because it can affect the quality and reliability of downstream analyses and experiments. Homology annotation is a powerful tool used to infer the function of a newly sequenced protein based on its similarity to proteins of known function. However, these annotations are not always perfect and can contain errors and biases, such as incorrect alignments or over-reliance on certain databases.

With this notebook you can visualise all information contained in the alignment result file.

So let's get into it.

---------------------------------------------

This Jupyter Notebook is designed to facilitate the analysis of homology-based annotation data produced by BLAST or Diamond software. It enables users to create insightful graphs and reports, simplifying the interpretation of tabular annotation files. To run this notebook, make sure you have the pandas, matplotlib, numpy, ipywidgets, and math libraries installed. They are already installed in the environment inside the docker container.

By engaging with interactive code examples and visual tools, users will learn to handle and visualize data derived from homology-based annotation workflows. This notebook allows users to swiftly and easily delve into their annotation data, revealing deeper insights into biological processes.

By following the instructions provided, users will be guided through the process of setting the parameters for their analysis. Once these parameters have been set, users can execute the notebook's cells one by one. It is strongly recommended that users follow the instructions step-by-step to ensure proper use of the tool.

1. **Import Libraries**

   Execute the following cell to import the essential libraries and initialize default settings.

2. **Configure Parameters**

   In this section, users need to set parameters related to the files they wish to analyze. Start by specifying the location of the results file. Next, provide the output format used during the alignment process.

   [Video Sketch on Output Format 6]

   Additionally, users can enter the initial part of the title for all generated graphs. Lastly, define the path for saving the output files.

3. **Filter Significant Hits**

   This cell helps users retain only the most significant hit for each sequence, discarding all other hits from the dataframe. You can set the number of hits to take into consideration in the following steps.

4. **Analyze Protein Function Hit Rate**

   This section allows users to create bar charts showcasing the most common protein functions identified across input sequences.

   - **Accession Graph**: Illustrates the number of hits associated with each protein accession in the BLAST or Diamond results.
     
     Run the cell to compute the accession rate.
   
   - **Select Annotation Database**: Choose the database used for annotation since storage systems vary across databases.
     
     Execute the cell to apply changes.

   - **Protein Function Bar Chart**: Generates a bar chart counting protein function names related to the annotation.
     
     Execute the cell below to generate the chart!

5. **Organism Hit Rate Analysis**

   Similar to the protein function analysis, this section provides bar charts to identify common organisms found in input sequences.

   - **Scientific Names Bar Chart**: Displays bar charts based on the frequency of organisms.
     
     Execute the cell below to create the chart!

6. **Hit Count Bar Chart**

   Create a bar chart showing the number of hits for each match in the annotation results.

7. **E-value Distribution Analysis**

   This section generates a histogram representing the distribution of E-values for all hits in the annotation results.

   Execute the cell below to create the histogram!

8. **Bit-score Distribution Analysis**

   Produce a histogram illustrating the distribution of bit-scores for each match in the annotation results.

9. **Length and Similarity Distribution**

   - **Length Distribution Chart**: Shows the distribution of sequence lengths, aiding in assessing alignment performance.
     
     Run the cell below to plot the chart!

   - **Similarity Distribution Chart**: Displays the distribution of sequence similarity percentages.
     
     Execute the cell below to plot the chart!
    
By following the steps outlined in this Jupyter Notebook, you can comprehensively analyze homology-based annotation results and gain valuable insights into your biological data. The visualizations and reports generated will assist in understanding the quality and significance of your annotations. We hope this notebook serves as a powerful tool in your research, enabling you to explore and interpret your data with ease. In the next video I will show you how to use the second notebook in our repository. Thanks for watching!

---------------------------------------------

This Jupyter Notebook support the analysis of homology-based annotation results, generated by BLAST or Diamond softwares, allowing users to generate informative graphs and plots to aid in the interpretation of tabular files obtained during the alignment process.

I hope you found this tutorial helpful and if you have any questions, feel free to leave them in the comments below. Thanks for watching!

*1 min*

## Jupyter notebook for BUSCO Result plot (BASE)
## Jupyter notebook for BUSCO Result plot (ADVANCED)
## Jupyter notebook for Comparing Annotation Results Across Databases Using Venn Diagrams
## Jupyter notebook for Generating Meaningful Graphs and Plots about your OrthoFinder Data


