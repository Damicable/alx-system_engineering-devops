
 Postmortem: SSH Key-Pair Access Outage Incident Report

Date: 26/09/2023

Summary:
On 26th September, 2023 at about 8:00pm GMT and lasted till 10:10pm GMT , an outage occurred affecting SSH access to my ALX provided servers using key-pair authentication. This postmortem report provides an analysis of the incident, its root causes, and the steps taken for resolution and future prevention.

> Incident Timeline:
At 8:00pm GMT,  as a transition into tech student, I was still unaware of the full details on the creation of the key-pair. 
This incident was first identified when I was unable to SSH into my ALX given server(Web-01) using key-pair authentication in out task on web server.

> Investigation:
At 8:45pm, I initiated an investigation to identify the cause of the SSH key-pair access outage.  The only analysis revealed that the SSH server was not recognizing valid key-pairs but do not know why and how to solve it.

> Action taken:
At about 9:20 I just figured out that in the previous SSH project, we were asked to create e and update the public key to our intranet profile which the key I provided was not approved.

So I googled to understand how to fix the key-pair to be approved on my intranet profile and I got my answer.
On my Ubuntu 20.04 command line, I got the key-pair using 'ssh-keygen -t rsa -b 2048 -C "annobidiegwu@gmail.com"' and boom! it worked. My profile was updated successfully

> Another Issue:
My profile was updated successfully and public key approved but it seems that I still could not ssh into my web server.

> Escalation:
By 9:37pm, my first idea outside google was to contact my learner peer by name Adedipe Ayooluwa, I explained my ordeal on my ssh command not recognizing any valid key pair I newly created.

> Issue detection:
We discovered that the generated keys were saved in the wrong path instead of being saved in ~/.ssh/id_rsa.pub), and the private key will be saved in the file ~/.ssh/id_rsa respectively.

> Root Causes:
Misconfiguration in SSH Authorized_Keys File:
The primary root cause was traced to a misconfiguration in the authorized_keys file used for key-pair authentication, leading to the rejection of valid key-pairs.

> Resolution:
By this time it was already 10:10pm, from my peer guidance, I was able to copy the key-pair from the wrong path to the  ~/.ssh/id_rsa.pub), and the private key copied to the file ~/.ssh/id_rsa. Hence, ssh into my server worked.

> Corrective and preventative measures:
. From my experience, as a new software tech student, I think generating ssh authorization key-pair in the command line of your working terminal is safer than generating the key-pair using PuTTY  keygen app.

> Task:
-  On your command line, run: ssh-keygen -t rsa -b 2048 -C "your_email@example.com"
-  Save the generated public key in the default location ~/.ssh/id_rsa.pub), and the private key will be saved in the file ~/.ssh/id_rsa respectively with out password
-  Then ssh @"username""IPaddress" press enter.
This automatically log you into your web server as provided  
Sincerely,

Obidiegwu Ann
