module.exports = {
  outputDir: 'html',
  assetsDir: './',
  publicPath: './',
  css: {
    loaderOptions: {
      css: {
        sourceMap: process.env.NODE_ENV !== "production" ? true : false
      }
    }
  }
};
