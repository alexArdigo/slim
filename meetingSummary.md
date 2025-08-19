# Meeting Summary – Log Flexibility


---

## Meeting Objective
The main goal of this meeting was to discuss improvements and alternatives to **increase flexibility in how logs are generated, organized, and queried**. Ideas were evaluated regarding default metrics, customization, search and sorting mechanisms, as well as storage methods and data retention policies.

---

## Topics Discussed

### 1. Flexibility of Metrics in Logs
- There was a need identified for a **default set of metrics** that will always be present in any log, regardless of user configuration.  
- In addition to the default metrics, we proposed allowing each user to **select additional metrics** they want to track, providing optional customization.  
- To meet this customization requirement, we discussed creating a **customizable function**, where users can pass their own metrics during execution.  
  - This function would combine user-defined metrics with the default metrics.  
  - This approach ensures both the consistency of key data and flexibility for specific use cases.  

### 2. Search and Sorting Mechanisms
- Implementing a **search mechanism within logs** was considered to facilitate information retrieval in large datasets.  
- We also discussed including a **sorting mechanism**, allowing logs to be ordered based on the metric chosen by the user.  
  - Example: sorting by execution time, number of parameters, accuracy, etc.  
- It was suggested that this functionality be **configurable**, letting users decide which columns or metrics will be used for sorting.  

### 3. Removal of Redundant Runs
- We identified scenarios where different runs might produce **identical logs**.  
- To prevent storage waste and redundancy, a mechanism for **automatic removal of duplicate runs** was discussed.  
- The exact method to identify identical logs (e.g., hash comparison, direct metric comparison) was not decided, but the usefulness of this feature was recognized.  

### 4. Log Storage Structure
- This topic remains open.  
- One proposal was to create **separate folders for each run**, properly labeled with relevant metadata (e.g., date, time, run ID, author).  
- Another possibility (not yet detailed) is the use of a **dedicated database** to organize and query logs.  
- No final decision was made; this topic will continue to be discussed in future meetings.  

### 5. Computational Cost and Retention Policy
- The **computational cost** of storing increasingly large log data was highlighted, especially in continuous experimentation scenarios.  
- The need for a **log retention policy** was discussed, including:
  - Criteria for **deleting old logs**.  
  - Determining which types of runs should be **prioritized for retention** (e.g., runs with the best performance or unique results).  
- No final decision was reached. This will be a **priority topic for the next meeting**.  

---

## Conclusions
- Consensus was reached on the importance of balancing **standardization and flexibility** in logs, ensuring minimum consistency while allowing customization.  
- Search, sorting, and duplicate removal mechanisms were well received and should be prioritized in upcoming implementation steps.  
- Storage remains undecided, but promising approaches include **folder-based organization** or a **database solution**.  
- Computational cost and log retention require further study and will be addressed in the next meeting.  

---

## Next Steps
1. Define the technical implementation of the **custom metrics function**.  
2. Specify requirements for **search and sorting mechanisms**.  
3. Detail the logic for **detecting and removing duplicate runs**.  
4. Evaluate and decide on the **log storage structure** (folders vs. database).  
5. Revisit **computational cost and old log retention policy** in the next meeting.  
