# Active Context: PollPal.nyc

## Current Work Focus

The current focus is on resolving a build issue with the Jekyll site. The build process was failing with the following error:

```
No such file or directory @ rb_sysopen - /opt/buildhome/repo/venv/bin/python (Errno::ENOENT)
```

This error occurred because Jekyll was attempting to process files in a Python virtual environment directory (`venv`) that doesn't exist or that Jekyll shouldn't be trying to access.

## Recent Changes

1. **Build Process Fix**:
   - Added `venv` to the `exclude` list in `_config.yml` to prevent Jekyll from attempting to process files in this directory
   - This should resolve the build failure and allow the site to be generated correctly

## Next Steps

1. **Verify Build Success**:
   - Run the Jekyll build process to confirm the fix resolves the issue
   - Check the generated site for any other potential issues

2. **Content Development**:
   - Review and potentially update the candidate stances in the quiz to ensure they accurately reflect current positions
   - Consider adding more detailed information about each candidate that users can access after seeing their results

3. **User Experience Improvements**:
   - Evaluate the quiz flow for potential usability improvements
   - Consider adding more visual elements to enhance engagement
   - Test the mobile responsiveness to ensure optimal experience across devices

4. **Performance Optimization**:
   - Analyze and optimize the JavaScript for the quiz functionality
   - Consider implementing lazy loading for non-critical resources
   - Optimize CSS by removing unused Tailwind classes

## Active Decisions and Considerations

### Build Process

The decision to exclude the `venv` directory in `_config.yml` was made because:
- Jekyll was attempting to process files in this directory, causing build failures
- Virtual environment directories contain binary files and executables that aren't relevant to the site content
- This is a common practice when using Jekyll with projects that might include Python components

### Architecture Decisions

1. **Static Site Generation**:
   - Continuing with Jekyll as the static site generator due to its simplicity and effectiveness for this use case
   - No need to introduce more complex frameworks as the current functionality is well-served by Jekyll

2. **JavaScript Approach**:
   - Maintaining the vanilla JavaScript approach for the quiz functionality
   - No immediate need to introduce a framework as the current implementation is clean and effective

### Content Strategy

1. **Quiz Questions**:
   - The current 14 questions cover key NYC issues and provide a good balance of topics
   - Questions are worded neutrally to avoid bias
   - Each question maps to specific candidate positions using a consistent scoring system

2. **Candidate Data**:
   - Candidate positions are stored as arrays with numeric values (+1, 0, -1)
   - This approach allows for simple calculation of alignment scores
   - Regular updates to candidate positions will be needed as the campaign progresses

### User Experience

1. **Progressive Disclosure**:
   - The current approach of showing one question at a time works well for mobile and desktop
   - Progress bar helps users understand how far they are in the quiz
   - Results visualization with percentage bars effectively communicates alignment

2. **Visual Design**:
   - Blue color scheme provides a neutral, trustworthy appearance
   - Card-based layout creates clear visual separation between components
   - Consistent styling throughout maintains a professional appearance
