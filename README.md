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

For simple posts without figures or equations, you might not need a preview. For information about previewing changes, see [below](#previewing-website-changes)

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

### Previewing website changes

There are two ways to get a preview of website changes before they go live online. The recommended method is to consult the test clone of the website, which lives online at rs-station.github.io/website-test. The test website is re-built automatically any time there is a pull request into the main branch of this repo. Any issues in content or formatting should be apparent from the test build, and these issues can be updated before the changes go live on the actual website. For contributing a blog post, this is all you should need to know!

#### Notes for writing HTML

Note that the syntactical sugar described here is only necessary when writting HTML, and can be ignored entirely when writing markdown.

The HTML infrastructure of the website is written such that the exact same code can build the website either at rs-station.github.io **or** rs-station.github.io/website-test. In order for this to work, HTML links must be specified as *relative* links with the following [Jekyll](https://jekyllrb.com/)/[Liquid](https://shopify.github.io/liquid/basics/introduction/) syntax:

```html
<a class="navbar-brand" href="{{ '/index.html' | relative_url}}"> 
```
This link will point to rs-station.github.io/index on the actual site, and to rs-station.github.io/website-test/index on the test site, as desired.

It is **incorrect** for any HTML links to be specified like this:

```html
<!-- this does not work! do not do this! -->
<a class="navbar-brand" href="/index.html"> 
```
because this link will always point to rs-station.github.io/index, even when it is supposed to point to rs-station.github.io/website-test/index.

You can find all the instances of this syntax by searching this repo for "relative_url".

#### Building Jekyll locally

The second (and not recommended) option is to run [Jekyll](https://jekyllrb.com/) yourself to build your own local copy of the site. Follow these instructions to serve the rs-station page locally for writing or development; be warned that this may involve a fair amount of setup and isntallation. 
 1. Install ruby and Jekyll by following the [instructions](https://jekyllrb.com/docs/) in the  Jekyll docs
 2. Install the `rs-station` specific dependencies by running: `gem install jekyll-font-awesome-sass github-pages`
 3. To start serving the site, run `bundle exec jekyll serve --livereload` in your local `rs-station.github.io` git repository
 4. Navigate to the "Server address" listed in your terminal window. The preview will live update after you make any changes. 
