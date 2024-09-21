-- sms_schema_and_data.sql

CREATE TABLE IF NOT EXISTS Contacts (
    contact_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    phone_number TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS Messages (
    message_id INTEGER PRIMARY KEY,
    sender_id INTEGER,
    receiver_id INTEGER,
    message_text TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (sender_id) REFERENCES Contacts(contact_id),
    FOREIGN KEY (receiver_id) REFERENCES Contacts(contact_id)
);

-- Insert dummy data into Contacts table
INSERT INTO Contacts (name, phone_number) VALUES
    ('John Doe', '1234567890'),
    ('Jane Smith', '9876543210'),
    ('Alice Johnson', '5555555555'),
    ('Bob Johnson', '1112223333'),
    ('Eva Davis', '4445556666'),
    ('Chris Williams', '7778889999'),
    ('Michael Brown', '3334445555'),
    ('Olivia White', '6667778888');

-- Insert dummy data into Messages table
INSERT INTO Messages (sender_id, receiver_id, message_text) VALUES
    (1, 2, 'Hello Jane! How are you?'),
    (2, 1, 'Hi John! I am good, thanks.'),
    (3, 1, 'Hey John, could you please call me when you get a chance?'),
    (3, 2, 'Hi Jane! Can we meet for lunch tomorrow?'),
    (1, 3, 'Sure Alice! What time works for you?'),
    (4, 1, 'Hey John, do you have any plans for the weekend?'),
    (2, 4, 'Not really Bob, just relaxing. How about you?'),
    (5, 6, 'Hi Chris! How is your day going?'),
    (6, 5, 'Hey Eva! It is going well, thanks.'),
    (7, 1, 'Hello John! Michael here. Lets catch up soon.'),
    (8, 2, 'Hi Jane! Olivia here. Do you have any weekend plans?');