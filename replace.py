#!/usr/bin/env python3
# filepath: /Users/mick/Projects/pollpal.nyc/transform_about.py

import re
import os

def transform_about_page():
    """
    Transform the about.md file with improved TailwindCSS styling.
    """
    input_file = '/Users/mick/Projects/pollpal.nyc/about.md'
    output_file = '/Users/mick/Projects/pollpal.nyc/about_styled.md'

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Preserve the front matter (YAML header)
    front_matter_pattern = r'^---\n(.*?)\n---\n'
    front_matter_match = re.search(front_matter_pattern, content, re.DOTALL)
    front_matter = front_matter_match.group(0) if front_matter_match else ''

    # Remove front matter for processing
    if front_matter:
        content = content.replace(front_matter, '', 1)

    # Create the main container with better styling
    new_container = '''
<div class="w-full max-w-3xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
    <div class="bg-blue-600 py-4 px-6">
        <h1 class="text-white font-bold text-2xl">About PollPal.nyc</h1>
    </div>
    <div class="p-6 space-y-6">
'''

    # Create the mission section with icon
    mission_section = '''
        <div class="flex items-center space-x-4 mb-6">
            <div class="bg-blue-100 p-3 rounded-lg">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
            </div>
            <div>
                <h2 class="font-semibold text-lg">Our Mission</h2>
                <p class="text-slate-600">Helping New Yorkers make informed voting decisions</p>
            </div>
        </div>
'''

    # Enhance section styling
    what_is_section = re.search(r'<section>.*?<h3[^>]*>What is[^<]*</h3>(.*?)</section>', content, re.DOTALL)
    if what_is_section:
        what_is_content = what_is_section.group(1)
        new_what_is_section = f'''
        <section class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
            <h3 class="text-xl font-semibold mb-3 text-blue-700">What is PollPal?</h3>
            {what_is_content}
        </section>
'''
        content = content.replace(what_is_section.group(0), new_what_is_section)

    # Enhance how it works section
    how_it_works_section = re.search(r'<section>.*?<h3[^>]*>How It Works</h3>(.*?)</section>', content, re.DOTALL)
    if how_it_works_section:
        how_it_works_content = how_it_works_section.group(1)
        new_how_it_works_section = f'''
        <section class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
            <h3 class="text-xl font-semibold mb-3 text-blue-700">How It Works</h3>
            {how_it_works_content}
        </section>
'''
        content = content.replace(how_it_works_section.group(0), new_how_it_works_section)

    # Create a table of contents for the detailed positions section
    toc_html = '''
            <!-- Table of Contents -->
            <div class="mb-8 p-4 bg-blue-50 rounded-lg">
                <h4 class="font-bold text-blue-800 mb-2">Quick Navigation</h4>
                <p class="text-sm text-slate-600 mb-3">Click on an issue to jump directly to candidate positions:</p>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-2">
                    <a href="#issue-1" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">1. Increasing NYPD officers</a>
                    <a href="#issue-2" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">2. Freezing or capping rents</a>
                    <a href="#issue-3" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">3. Mental health vs policing for crime</a>
                    <a href="#issue-4" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">4. Free childcare for families</a>
                    <a href="#issue-5" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">5. Local residents vs new arrivals</a>
                    <a href="#issue-6" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">6. Major housing goals</a>
                    <a href="#issue-7" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">7. Charter schools expansion</a>
                    <a href="#issue-8" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">8. Free public buses</a>
                    <a href="#issue-9" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">9. Shrinking city government</a>
                    <a href="#issue-10" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">10. Mandating mental health treatment</a>
                    <a href="#issue-11" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">11. Converting spaces to housing</a>
                    <a href="#issue-12" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">12. Police reform priorities</a>
                    <a href="#issue-13" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">13. Attracting businesses</a>
                    <a href="#issue-14" class="text-blue-600 hover:text-blue-800 hover:underline text-sm">14. Climate goals investment</a>
                </div>
            </div>
'''

    # Process each of the 14 issues
    issues = []
    for i in range(1, 15):
        # Find each issue section
        issue_pattern = rf'<h3[^>]*>\s*{i}\.\s*(.*?)</h3>(.*?)(?=<h3|$)'
        issue_match = re.search(issue_pattern, content, re.DOTALL)

        if issue_match:
            issue_title = issue_match.group(1).strip()
            issue_content = issue_match.group(2).strip()

            # Replace the candidate list with styled elements
            candidate_pattern = r'<li><strong>([^<]+):</strong>(.*?)</li>'
            styled_candidates = ""

            for candidate_match in re.finditer(candidate_pattern, issue_content, re.DOTALL):
                candidate_name = candidate_match.group(1)
                candidate_position = candidate_match.group(2)

                styled_candidate = f'''
                    <div class="p-3 border-l-4 border-blue-500 bg-blue-50">
                        <h4 class="font-bold">{candidate_name}:</h4>
                        <p class="text-slate-700">{candidate_position}</p>
                    </div>'''

                styled_candidates += styled_candidate

            # Create the styled issue section
            styled_issue = f'''
            <!-- Issue {i} -->
            <div id="issue-{i}" class="mb-10 pb-6 border-b border-gray-200">
                <h3 class="text-lg font-semibold mb-3 bg-blue-100 p-2 rounded-md">{i}. {issue_title}</h3>
                <div class="space-y-4">
                    {styled_candidates}
                </div>
            </div>
'''
            issues.append(styled_issue)

    # Begin the detailed positions section
    detailed_positions = f'''
        <section class="bg-white p-6 rounded-lg shadow-sm border border-gray-100">
            <h3 class="text-xl font-semibold mb-3 text-blue-700">Detailed Positions</h3>

            {toc_html}

            {"".join(issues)}

            <div class="mt-8 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                <p class="text-sm text-gray-600">
                    Each candidate's positions are summarized above with sources from official statements, campaign platforms, and news reporting for verification. These stances span a wide spectrum from strongly pro-policing to reform-focused, from business-friendly to community-first, and from climate-cautious to climate-warrior, reflecting the ideological diversity in the 2025 NYC mayoral field.
                </p>
            </div>
        </section>
'''

    # Create the contact section
    contact_section = '''
        <div class="bg-blue-50 p-5 rounded-lg border border-blue-100 mt-6 shadow-sm">
            <h3 class="font-semibold text-lg mb-3 text-blue-800">Contact Us</h3>
            <p class="text-slate-700 mb-3">
                Have questions, feedback, or suggestions? We'd love to hear from you!
            </p>
            <p class="text-slate-700">
                Email: <a href="mailto:info@PollPal.nyc" class="text-blue-600 hover:underline font-medium">info@PollPal.nyc</a>
            </p>
        </div>
'''

    # Add back to top button
    back_to_top = '''
<!-- Back to top button -->
<div class="fixed bottom-4 right-4">
    <a href="#" class="bg-blue-600 hover:bg-blue-700 text-white p-3 rounded-full shadow-lg flex items-center justify-center">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 10l7-7m0 0l7 7m-7-7v18" />
        </svg>
    </a>
</div>
'''

    # Combine everything
    transformed_content = (
        front_matter +
        new_container +
        mission_section
    )

    # Find or replace existing "what is" and "how it works" sections
    if "What is PollPal?" in transformed_content:
        pass  # Already processed
    else:
        transformed_content += '\n' + new_what_is_section

    if "How It Works" in transformed_content:
        pass  # Already processed
    else:
        transformed_content += '\n' + new_how_it_works_section

    # Add the detailed positions section
    transformed_content += '\n' + detailed_positions

    # Add the contact section and closing tags
    transformed_content += '\n' + contact_section + '\n    </div>\n</div>\n'

    # Add back to top button
    transformed_content += '\n' + back_to_top

    # Write the transformed content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(transformed_content)

    print(f"Transformation complete! New file saved to: {output_file}")
    print("Review the new file and if it looks good, you can replace the original:")
    print(f"mv {output_file} {input_file}")

if __name__ == "__main__":
    transform_about_page()