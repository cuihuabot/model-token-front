const fs = require('fs');
const path = require('path');

function generatePostsManifest() {
  const jekyllDir = './jekyll-site';
  const postsDir = path.join(jekyllDir, '_posts');
  const manifestPath = path.join(postsDir, 'posts-manifest.json');
  
  if (!fs.existsSync(postsDir)) {
    console.log('Posts directory does not exist:', postsDir);
    return;
  }
  
  const postFiles = fs.readdirSync(postsDir);
  const posts = [];
  
  for (const file of postFiles) {
    if (file.endsWith('.html') && file !== 'posts-manifest.json') {
      const filePath = path.join(postsDir, file);
      const content = fs.readFileSync(filePath, 'utf8');
      
      // Extract front matter
      const frontMatterMatch = content.match(/^---\n([\s\S]*?)\n---/);
      let title = file.replace('.html', '');
      let model = 'unknown';
      let config = 'unknown';
      let date = 'unknown';
      
      if (frontMatterMatch) {
        const frontMatter = frontMatterMatch[1];
        const titleMatch = frontMatter.match(/title:\s*"(.+)"/);
        const modelMatch = frontMatter.match(/model:\s*(.+)/);
        const configMatch = frontMatter.match(/config:\s*(.+)/);
        const dateMatch = frontMatter.match(/date:\s*(.+)/);
        
        if (titleMatch) title = titleMatch[1];
        if (modelMatch) model = modelMatch[1].trim();
        if (configMatch) config = configMatch[1].trim();
        
        // Extract date in YYYY-MM-DD format from the date field
        if (dateMatch) {
          const dateValue = dateMatch[1].trim();
          // Parse the date to get YYYY-MM-DD format
          const dateObj = new Date(dateValue);
          if (!isNaN(dateObj.getTime())) {
            date = dateObj.toISOString().split('T')[0];
          } else {
            // If parsing fails, try to extract from filename
            const dateFromFilename = file.match(/^\d{4}-\d{2}-\d{2}/);
            if (dateFromFilename) {
              date = dateFromFilename[0];
            }
          }
        }
      }
      
      posts.push({
        filename: file,
        title,
        model,
        config,
        date
      });
    }
  }
  
  // Sort posts by date (newest first)
  posts.sort((a, b) => {
    const dateA = new Date(a.date);
    const dateB = new Date(b.date);
    return dateB - dateA; // Descending order (newest first)
  });
  
  // Write the manifest file
  fs.writeFileSync(manifestPath, JSON.stringify(posts, null, 2));
  console.log(`Generated posts-manifest.json with ${posts.length} entries`);
  
  return posts;
}

// Run if called directly
if (require.main === module) {
  generatePostsManifest();
}

module.exports = generatePostsManifest;