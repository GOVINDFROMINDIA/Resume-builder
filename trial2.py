from docx import Document

def replace_content_below_heading(doc, heading_text, replacement_text):
    found_heading = False

    for paragraph in doc.paragraphs:
        if found_heading:
            # Replace content below the heading
            if paragraph.text.strip():  # Skip empty paragraphs
                paragraph.text = replacement_text
                break  # Stop after replacing the content

        if paragraph.text.strip() == heading_text:
            found_heading = True  # Set flag when the heading is found
    print(found_heading)
def insert_content_into_template():
    # Path to your downloaded resume template
    template_path = "template_1.docx"

    # Your content for education, skills, etc. with respective headings
    content = {
        "EDUCATION_HEADING": "Education",
        "Education": "Brown University",
        "SKILLS_HEADING": "Skills",
        "Skills": "data Analytics and swimming",
        # Add more headings and their corresponding content
    }

    # Load the template document
    doc = Document(template_path)

    # Replace content below each heading
    for heading_text, replacement_text in content.items():
        replace_content_below_heading(doc, heading_text, replacement_text)

    # Save the modified document with the new content
    output_path = "C:/Users/91977/Documents/modified_resume.docx"
    doc.save(output_path)

# Call the function to insert your content into the template
insert_content_into_template()
