🧠 Distributed Word Count System
The Distributed Word Count System is a simple Python-based project that demonstrates the concept of distributed computing using a Master-Worker architecture.
It splits a large text into smaller chunks, distributes them across multiple worker nodes, and aggregates the results to compute word frequencies efficiently.
This project helps in understanding parallel processing, REST APIs, and distributed system basics.

✨ Features

📊 Word Count Processing: Counts frequency of words from large text input
⚡ Distributed Execution: Splits workload across multiple worker nodes
🔗 REST API Communication: Uses HTTP requests between master and workers
🧵 Parallel Processing Simulation: Improves performance over single-threaded execution
🧪 Performance Comparison: Compare single-thread vs distributed execution


📦 Prerequisites
Make sure you have:

Python 3.x
pip3 (Python package manager)
Linux / Unix environment (or Horizon server)


🛠️ Technologies Used
Backend

Python 3
Flask – Worker API server
Requests – Communication between master and workers

Concepts

Distributed Systems
MapReduce (basic simulation)
Client-Server Architecture


⚙️ Installation
1. Clone repository

git clone https://github.com/your-username/distributed-word-count.git

2. Navigate to project

cd distributed-word-count

3. Install dependencies

pip3 install flask requests
``
(If no sudo access)
python3 -m pip install --user flask requests

▶️ Running the Project
✅ Step 1: Start Worker Nodes
Run terminal 
python3 worker.py 5001 & python3 worker.py 5002 & python3 compare.py
``

🔄 How It Works

The master node divides the input text into chunks
Each chunk is sent to different worker nodes via HTTP
Workers process text and return word counts
The master aggregates results into a final count
Execution time is compared with single-threaded processing


📊 Example Output
Single-threaded time: 2.1345s
Distributed time: 1.0234s


📂 Project Structure
distributed-word-count/
│
├── worker.py     # Worker node (Flask API for processing text)
├── master.py     # Master logic for distributing tasks
├── compare.py    # Performance comparison script
└── README.md     # Project documentation


✅ Example Use Cases

Learning distributed computing concepts
Simulating MapReduce systems
Understanding REST-based communication
Performance optimization experiments


🚀 Future Enhancements

Multi-machine (real distributed) support
Docker containerization
Kubernetes deployment
Load balancing between workers
GUI dashboard for monitoring


🤝 Contributing
Contributions are welcome!
Steps:

Fork the repository
Create a new branch
Make changes
Submit a pull request


📜 License

This project is licensed under the MIT License.
``

🙏 Acknowledgments

Python community
Flask framework contributors
Open-source ecosystem
Academic learning resources on distributed systems


🔗 Repository Link
git clone https://github.com/tfregixx/distributed-word-count.git

