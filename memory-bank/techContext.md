# Technical Context: PollPal.nyc

## Technologies Used

### Core Technologies

1. **Jekyll (v4.3.2)**
   - Static site generator built on Ruby
   - Uses Liquid templating language
   - Processes Markdown content with YAML front matter
   - Handles site structure and navigation

2. **HTML5**
   - Semantic markup for accessibility and SEO
   - Modern document structure
   - Canvas for potential data visualizations

3. **CSS**
   - **Tailwind CSS**: Utility-first CSS framework
   - Responsive design principles
   - Custom components for quiz interface
   - Animations for interactive elements

4. **JavaScript**
   - Vanilla JS (no framework dependencies)
   - DOM manipulation for quiz functionality
   - Event handling for user interactions
   - Scoring algorithm for candidate matching

### Supporting Technologies

1. **Ruby Gems**
   - jekyll-feed: Generates an RSS feed
   - jekyll-seo-tag: Improves SEO metadata
   - webrick: Local development server

2. **Font Awesome**
   - Icon library for UI elements
   - SVG-based for performance and scalability

3. **Google Fonts**
   - Inter font family for typography
   - Optimized for web performance

4. **Version Control**
   - Git for source code management
   - GitHub for repository hosting

## Development Setup

### Local Development Environment

1. **Prerequisites**
   - Ruby (v2.7.0 or higher)
   - Bundler (for managing Ruby dependencies)
   - Jekyll (v4.3.2)
   - Git (for version control)

2. **Installation Steps**
   ```bash
   # Clone the repository
   git clone [repository-url]

   # Install dependencies
   bundle install

   # Start the development server
   bundle exec jekyll serve
   ```

3. **Development Workflow**
   - Edit Markdown content and templates
   - Jekyll automatically rebuilds on file changes
   - Preview at http://localhost:4000
   - Commit changes to Git repository

### Build Process

1. **Jekyll Build**
   - Converts Markdown to HTML
   - Processes Liquid templates
   - Applies layouts and includes
   - Generates static site in `_site` directory

2. **Asset Pipeline**
   - CSS processing and optimization
   - JavaScript bundling (if needed)
   - Image optimization
   - File fingerprinting for cache busting

3. **Deployment**
   - Static files deployed to web hosting
   - No server-side processing required
   - CDN distribution for performance

## Technical Constraints

### Performance Constraints

1. **Page Load Time**
   - Target: < 2 seconds initial load
   - Minimize JavaScript execution time
   - Optimize image sizes and formats
   - Leverage browser caching

2. **Mobile Performance**
   - Responsive to various screen sizes
   - Touch-friendly interface elements
   - Reduced network payload for mobile users

### Browser Compatibility

1. **Target Browsers**
   - Modern browsers (Chrome, Firefox, Safari, Edge)
   - iOS Safari and Android Chrome
   - IE11 not supported

2. **Progressive Enhancement**
   - Core functionality works without JavaScript
   - Enhanced experience with JavaScript enabled
   - Fallbacks for older browsers where feasible

### Security Considerations

1. **Static Site Advantages**
   - No server-side code execution
   - No database to compromise
   - Reduced attack surface

2. **Content Security**
   - No user data collection or storage
   - No authentication requirements
   - External resources (CDNs) properly secured

## Dependencies

### Direct Dependencies

1. **Production Dependencies**
   - jekyll (~> 4.3.2)
   - jekyll-feed (~> 0.12)
   - jekyll-seo-tag (~> 2.8)
   - webrick (~> 1.8)

2. **Development Dependencies**
   - None specified in Gemfile

### External Services

1. **CDN Services**
   - Tailwind CSS via CDN
   - Google Fonts
   - Font Awesome

2. **Hosting**
   - Static site hosting platform (not specified)
   - Domain registrar for PollPal.nyc

## Technical Debt and Considerations

1. **Current Technical Debt**
   - Build process issue with venv directory (fixed by excluding in _config.yml)
   - Potential optimization of JavaScript for quiz functionality
   - CSS could be further optimized by removing unused Tailwind classes

2. **Future Considerations**
   - Potential migration to newer Jekyll versions
   - Consideration of build-time optimization for assets
   - Possible implementation of PWA features for offline access
   - Automated testing for quiz functionality
