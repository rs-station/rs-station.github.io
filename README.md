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
 - You may enable latex rendering through mathjax by adding the following line to your post's front matter,

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

