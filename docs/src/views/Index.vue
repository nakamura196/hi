<template>
  <div class="wrapper">
    <parallax class="section page-header header-filter" :style="headerStyle">
      <div class="container">
        <div class="md-layout">
          <div
            class="md-layout-item md-size-50 md-small-size-70 md-xsmall-size-100"
          >
            <h1 class="title">史料集版面ギャラリー</h1>
            <h4>
              東京大学史料編纂所編を改変
            </h4>
          </div>
        </div>
      </div>
    </parallax>
    <div class="main main-raised">
      <div class="section">
        <div class="container">
          <div class="md-layout">
            
            <div
              class="md-layout-item md-size-66 md-xsmall-size-100 mx-auto text-center"
            >
              <h2 class="title text-center" id="about">このサイトについて</h2>
              <h5 class="description">
                本サイトは、<a href="https://www.hi.u-tokyo.ac.jp/publication/dip/index.html">史料集版面ギャラリー</a>（東京大学史料編纂所編）を改変し、IIIFコレクションを用いて史料を閲覧可能なサイトです。
              </h5>
            </div>
          </div>
        <div class="features text-center">
            <div class="md-layout">
              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="info">
                  <h4 class="info-title">IIIF</h4>
                  <p>
                    <a href="https://iiif.io/api/presentation/2.1/#collection">IIIF Collection</a>を使って史料群の階層を表現しています。<a href="https://iiif.io/api/image/2.1/">IIIF Image API</a>は利用していないため、一部のViewerでは閲覧できない点にご注意ください。
                  </p>
                </div>
              </div>
              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="info">
                  <h4 class="info-title">OCR &amp; TEI</h4>
                  <p>
                    <a href="https://cloud.google.com/vision/">Google Could Vision API</a>によるOCRテキストを用いた全文検索機能を提供します。テキスト情報は<a href="https://tei-c.org/">TEI</a>で保持し、検索機能には<a href="https://iiif.io/api/search/1.0/">IIIF Search API</a>を用いています。
                  </p>
                </div>
              </div>
              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="info">
                  <h4 class="info-title">Open Data</h4>
                  <p>
                    <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>ライセンスで公開されているオープンデータを利用しています。本サイトで公開するデータについても、<a href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA</a>ライセンスで利用可能です。
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="section text-center">
        <div class="container">
          <h2 class="title">Viewers</h2>
          <div class="team">
            <div class="md-layout">

              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="team-player">
                  <md-card class="md-card-plain">
                    <div class="md-layout-item md-size-50 mx-auto">
                      <a href="https://www.kanzaki.com/works/2016/pub/image-annotator?u=https://nakamura196.github.io/hi/data/collection.json">
                      <img
                        :src="teamImg3"
                        alt="Thumbnail Image"
                        class="img-raised rounded-square img-fluid"
                      />
                      </a>
                    </div>
                    <h4 class="card-title">
                      Image Annotator
                    </h4>

                    <md-card-content>
                      <p class="card-description">
                        神崎正英氏が開発している<a href="https://www.kanzaki.com/works/2016/pub/image-annotator">Image Annotator</a>を用いて閲覧します。
                      </p>
                    </md-card-content>

                    <a type="button" class="md-button md-success md-theme-default" href="https://www.kanzaki.com/works/2016/pub/image-annotator?u=https://nakamura196.github.io/hi/data/collection.json">
                      <div class="md-ripple">
                        <div class="md-button-content">閲覧する</div>
                      </div>
                    </a>
                  </md-card>
                </div>
              </div>

              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="team-player">
                  <md-card class="md-card-plain">
                    <div class="md-layout-item md-size-50 mx-auto">
                      <a href="http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/collection.json">
                      <img
                        :src="teamImg1"
                        alt="Thumbnail Image"
                        class="img-raised rounded-square img-fluid"
                      />
                      </a>
                    </div>
                    <h4 class="card-title">
                      Universal Viewer
                    </h4>

                    <md-card-content>
                      <p class="card-description">
                        <a href="https://universalviewer.io/">Universal Viewer</a>を用いて閲覧します。
                      </p>
                    </md-card-content>

                    <a type="button" class="md-button md-success md-theme-default" href="http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/collection.json">
                      <div class="md-ripple">
                        <div class="md-button-content">閲覧する</div>
                      </div>
                    </a>
                  </md-card>
                </div>
              </div>
              <div class="md-layout-item md-medium-size-33 md-small-size-100">
                <div class="team-player">
                  <md-card class="md-card-plain">
                    <div class="md-layout-item md-size-50 mx-auto">
                      <a href="https://nakamura196.github.io/portal_pro/common/javala/?collection=https://nakamura196.github.io/hi/data/collection.json">
                      <img
                        :src="teamImg2"
                        alt="Thumbnail Image"
                        class="img-raised rounded-square img-fluid"
                      />
                      </a>
                    </div>
                    <h4 class="card-title">
                      Javala
                    </h4>

                    <md-card-content>
                      <p class="card-description">
                        Durham Universityが開発している<a href="https://github.com/durham-university/jalava">Jalava</a>を用いて閲覧します。（※ IIIF Image APIに非対応のため、現時点では本Viewerでの画像閲覧はできません。）
                      </p>
                    </md-card-content>

                    <a type="button" class="md-button md-success md-theme-default" href="https://nakamura196.github.io/portal_pro/common/javala/?collection=https://nakamura196.github.io/hi/data/collection.json">
                      <div class="md-ripple">
                        <div class="md-button-content">閲覧する</div>
                      </div>
                    </a>
                  </md-card>
                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  bodyClass: 'landing-page',
  props: {
    header: {
      type: String,
      default: require('@/assets/img/bg7.jpg')
    },
    teamImg1: {
      type: String,
      default: require('@/assets/img/faces/avatar.jpg')
    },
    teamImg2: {
      type: String,
      default: require('@/assets/img/faces/christian.jpg')
    },
    teamImg3: {
      type: String,
      default: require('@/assets/img/faces/kendall.jpg')
    }
  },
  data () {
    return {
      name: null,
      email: null,
      message: null
    }
  },
  computed: {
    headerStyle () {
      return {
        backgroundImage: `url(${this.header})`
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.md-card-actions.text-center {
  display: flex;
  justify-content: center !important;
}
.contact-form {
  margin-top: 30px;
}

.md-has-textarea + .md-layout {
  margin-top: 15px;
}
</style>
