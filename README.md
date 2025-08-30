# Reciprocal Space Station Website

Organization website for Reciprocal Space Station


### Writing Blog Posts
Reciprocal Space Station encourages developers to contribute [blog posts](rs-station.github.io/blog). We're flexible on the formatting, but we suggest following these __guidelines__
 - Blog posts are markdown files in the format `rs-station.github.io/_posts/YYYY-MM-DD-post-title.md`. 
 - Posts begin with a YAML front matter block such as

        ---
        layout: post
        title: A Short Title
        subtitle: A Longer Subtitle
        author: Your Name
        usemathjax: true
        ---
 - You may enable latex rendering through mathjax by adding the following line to your post's front matter

        usemathjax: true
 - If the post contains media such as images, those should be located in `rs-station-github.io/assets/posts/YYYY-MM-DD-post-title`.
 - Use the `blog-image`, `blog-caption` or `blog-image-wide`, `blog-caption-wide` attributes to format images. For example,

        ![Systematic errors in rotation data](/assets/posts/2024-07-31-multivariate-wilson/systematic_error.png){: .blog-image} 
        Example of systematic errors in conventional diffraction data from [Dalton et al](https://doi.org/10.1038/s41467-022-35280-8). [(CC-BY license)](https://creativecommons.org/licenses/by/4.0/)
        {: .blog-caption}
 - Inlude the licenses of images from papers or preprints.

For simple posts without figures or equations, you might not need a preview. For more complicated posts, you can run [Jekyll](https://jekyllrb.com/) locally to get a live preview. Follow these instructions to serve the rs-station page locally for writing or development. 
 1. Install ruby and Jekyll by following the [instructions](https://jekyllrb.com/docs/) in the  Jekyll docs
 2. Install the `rs-station` specific dependencies by running: `gem install jekyll-font-awesome-sass github-pages`
 3. To start serving the site, run `bundle exec jekyll serve --livereload` in your local `rs-station.github.io` git repository
 4. Navigate to the "Server address" listed in your terminal window. The preview will live update after you make any changes. 

### Adding references
References from `_data/publications.yml` are automatically included in the "Publications and Citing" tab of the rs-station page. Adding a reference just requires adding a properly formatted entry `yml`. There are two types of entries dictated by what "section" they are affiliated with. "cite" entries are for primary citations for software packages and will be rendered in the first section of the webpage. A new cite entry has the following format,

```yml
- nickname: reckless
  section: cite
  package: Reckless
  title: Online Maximization of Paperclips
  authors: "**Devin M. Bolton**, Zach B. Micemen, Derk R. Hoekstra"
  url: https://doi.org/1l.1111/2033.01.12.632630
  info: Nature, 2033
```

For other publications that were written by reciprocal astronauts and/or using rs-station software, add a "pubs" entry using the following format,


```yml
- nickname: reckless
  section: pubs
  title: Online Maximization of Paperclips
  authors: "**Devin M. Bolton**, Zach B. Micemen, Derk R. Hoekstra"
  url: https://doi.org/1l.1111/2033.01.12.632630
  info: Nature, 2033
```

The key differences are that the "section" value is different and that "cite" entries must include a "package". The formatting is fairly relaxed, but generally, we advise
 - Write authors in "First M. Last" format
 - Comma separate author names
 - use bold text (ie. `**First A. Author**, Second B. Author, Third C. Author`) to highlight the first author
 - Use a doi for the url whenever available

