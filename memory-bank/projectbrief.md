# Project Brief: PollPal.nyc

## Overview
PollPal.nyc is a Jekyll-based website designed to help New York City residents understand where mayoral candidates stand on key issues. The site features an interactive quiz that matches voters with candidates who share their values and policy preferences.

## Core Requirements

### Functional Requirements
1. **Interactive Quiz**: A 14-question quiz on key NYC issues that users can complete to find matching candidates
2. **Candidate Matching Algorithm**: Calculate alignment scores between user responses and candidate positions
3. **Results Display**: Show users how well they match with each candidate
4. **Mobile-Responsive Design**: Ensure the site works well on all device sizes
5. **About Page**: Provide information about the project's purpose and methodology

### Technical Requirements
1. **Jekyll-Based**: Built with Jekyll static site generator
2. **Tailwind CSS**: Use Tailwind for styling and responsive design
3. **JavaScript Functionality**: Handle quiz logic and candidate matching
4. **Deployment**: Deploy to a hosting platform with the PollPal.nyc domain

## Project Goals
1. Create a non-partisan platform for voter education
2. Help NYC residents make informed voting decisions
3. Increase voter engagement and understanding of candidate positions
4. Provide a simple, intuitive user experience
5. Ensure accurate representation of candidate stances

## Target Audience
- NYC residents eligible to vote in mayoral elections
- Politically engaged citizens seeking to understand candidate positions
- Undecided voters looking for guidance on which candidate aligns with their views

## Success Metrics
1. User engagement with the quiz (completion rate)
2. Time spent on the site
3. Social sharing of quiz results
4. Positive user feedback
5. Accuracy of candidate position representation

## Timeline
The site should be fully functional and deployed before the NYC mayoral election campaign season begins in earnest.

## Current Status
The site is currently in development with the core quiz functionality implemented. The build process has an issue with Jekyll trying to process files in a non-existent Python virtual environment directory, which has been fixed by excluding the `venv` directory in the `_config.yml` file.
