# Automated Text Data Extraction and Form Filling System

![Project Preview](https://github.com/kirudang/Automated_Text_Extraction/assets/91911269/86004f85-f431-49b7-8ad5-09f69776e09d)

In today's data-driven world, efficiently extracting and processing information from unstructured text data is essential for businesses. This project introduces an Automated Text Data Extraction and Form Filling System, designed to streamline the extraction of valuable information from various text formats and automate form filling processes. By combining multiple techniques, including OCR, language models, NER, and regular expressions, this system aims to enhance data accuracy and accelerate business operations.

## Table of Contents
- [Introduction](#Introduction)
- [Project Structure](#Project-Structure)
- [Motivation](#Motivation)
- [Use-Cases](#Use-Cases)
- [Methods](#Methods)
  - [Data Extraction](#Data-Extraction)
  - [Information Capture](#Information-Capture)
  - [Automation](#Automation)
- [Getting Started](#Getting-Started)
- [Dependencies](#Dependencies)
- [Contributing](#Contributing)
- [License](#License)

## Introduction

In an era where data fuels business operations, the need for accurate and efficient text data extraction cannot be overstated. This project addresses this challenge by introducing an Automated Text Data Extraction and Form Filling System, designed to streamline information extraction and eliminate manual data entry errors. Whether it's parsing contracts, invoices, or handwritten notes, this system offers a comprehensive solution for businesses seeking to leverage automation for growth.

## Project Structure

The project is structured into several key components:

1. **Motivation**: Explains the driving forces behind the development of this system, including the aspiration to minimize errors and accelerate business growth.

2. **Use-Cases**: Provides real-world scenarios where this system can add significant value, from job applications to legal document analysis.

3. **Methods**: Explores the methodologies employed in the system, including Data Extraction, Information Capture, and Automation.

4. **Getting Started**: Offers instructions on how to set up and utilize this system for your specific needs.

5. **Dependencies**: Lists the necessary libraries and tools required to run the system successfully.

6. **Contributing**: Encourages contributions to enhance the project and address potential improvements or issues.

7. **License**: States the project's licensing information.

## Motivation

The motivations behind developing an OCR and Language Model for Accurate Text Data Extraction are multifaceted, each driven by the aspiration to harness the power of automation, minimize errors, and accelerate business growth.

## Use-Cases

Here are some concrete use-cases where such a system can be incredibly valuable:
- Job application: Automatically extract and fill candidate data from uploaded CVs.
- Faster Quotation Process: Expedite quotation generation in industries like insurance, construction, or manufacturing.
- Legal Document Analysis: Assist legal professionals in parsing through extensive legal documents.
- Inventory Management: Automate tracking of inventory by extracting product information from invoices.
- Medical Records Digitization: Accelerate the process of digitizing patient records for quick access to healthcare information.

## Methods

The project employs various methods for data extraction, information capture, and automation.

### Data Extraction

- Optical Character Recognition (OCR): Utilized for text recognition.
- PDF2 Package: Efficiently extracts text from different PDF formats.

### Information Capture

- Regular Expression Approach: Traditional method for structured input data.
- Rule-based Approach: Pattern-based extraction for specific information.
- NER (Named Entity Recognition) Model: Leverages spaCy's NER model to identify and capture entities.
- Hybrid Approach: Combines multiple methods for robust extraction.
- Language Model Approach: Utilizes large language models like ChatGPT API for context-aware data extraction.

### Automation

It depends your company technology, but this step is easy. In this project, I use Selenium package to populate data in required fields.

https://github.com/kirudang/Automated_Text_Extraction/assets/91911269/363b411a-5630-4de2-859b-580d0ec05167

## Getting Started

To utilize the Automated Text Data Extraction and Form Filling System, follow these steps:

1. Clone the repository to your local machine.

2. Navigate to the project directory.

3. Set up the required dependencies as specified in the project documentation.

4. Explore the provided scripts and adapt them to your specific use cases.

## Dependencies

The project relies on various Python libraries and tools, including but not limited to:
- Optical Character Recognition (OCR)
- spaCy
- Regular Expressions
- Named Entity Recognition (NER)
- ChatGPT API

These dependencies are documented in detail in the project's documentation.

## Contributing

Contributions to this project are welcome. If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Your input is invaluable in enhancing this system.

## License

This project is licensed under the [MIT License](LICENSE). Please refer to the license file for more details.
