CREATE DATABASE IF NOT EXISTS donation_database;
USE donation_database;

CREATE TABLE IF NOT EXISTS donations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fullName VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(20),
    donationType VARCHAR(20) NOT NULL,
    companyName VARCHAR(255),
    creditCardNumber VARCHAR(16) NOT NULL,
    cvv VARCHAR(3) NOT NULL,
    expirationDate VARCHAR(5) NOT NULL,
    billingPostalCode VARCHAR(10) NOT NULL,
    donationAmount VARCHAR(20) NOT NULL,
    donationFrequency VARCHAR(20) NOT NULL
);