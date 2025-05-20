# 🛡️ SecureCheck – Password Strength & Cracking Analysis Tool

SecureCheck is a real-world cybersecurity project that allows users to analyze the strength of a password, simulate brute-force attacks, and perform dictionary-based cracking using John the Ripper (JtR) — all via a responsive and modern UI.

## 🎯 Features

- 🔑 Password Input Interface with secure styling and show/hide toggle  
- ⚙️ Real Entropy & Strength Estimation based on password complexity  
- 🔍 Brute-force Time Estimation using simulated keyspace math  
- 📚 John the Ripper Dictionary Attack Integration with rockyou.txt  
- 🚦 Strength Meter + Suggestions to improve user passwords  
- 📊 Detailed Results Section for cracked status, entropy, time to crack, and more  

## 🛠 Installation

Follow these steps to run the project locally:

1. **Clone the Repository**

   `git clone https://github.com/your-username/securecheck.git`  
   `cd securecheck`

2. **Install Dependencies**

   `pip install flask flask-cors`

3. **Download John the Ripper and Add to PATH**

   Download from https://github.com/openwall/john  
   Make sure the john command works globally via terminal.

4. **Run the Flask App**

   `python app.py`

5. **Access the Web App**

   Open your browser and go to: [http://localhost:5000](http://localhost:5000)

## ⚙️ How It Works

- User enters a password in the frontend UI.
- The password is hashed (MD5) and saved to `hashes/password.txt`.
- John the Ripper runs a dictionary attack on the hash using `rockyou.txt`.
- Python calculates:
  - Entropy
  - Brute-force time estimation
  - Password strength
- Results are displayed in a visually styled output panel.

## 📁 Wordlist Disclaimer

This project uses `rockyou.txt` for performing dictionary attacks via John the Ripper.

However, due to GitHub's file size limit of 100MB, the `rockyou.txt` file is **not included** in this repository.

### 🔽 How to Set It Up

1. Download `rockyou.txt` from the official [SecLists GitHub repository](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz)
2. Extract the archive to obtain `rockyou.txt`
3. Place the file inside the `/wordlists` folder in this project

Once added, the dictionary attack functionality using John the Ripper will work as expected.

## 📦 Future Enhancements

- 🧠 AI-generated password suggestions based on analysis  
- 🌐 WebSocket-based cracking feedback  
- 🔐 Support for additional hash formats like SHA-1, bcrypt  

## Contact

If you have any questions or suggestions regarding this project, feel free to contact us at [atharvat.code@gmail.com](mailto:atharvat.code@gmail.com).
