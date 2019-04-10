<template>
  <div class="wrapper">
    <parallax
      class="section page-header header-filter"
      :style="headerStyle"
    ></parallax>

    <div class="main main-raised">
      <div class="section profile-content">
        <div class="container">
          <div class="profile-tabs">
            <div
                  class="md-layout-item md-size-66 md-xsmall-size-100 mx-auto text-center"
                >
                  <h2 class="title text-center">テキスト検索可能な史料一覧</h2>

                  <p class="text-muted">順次追加中です。<a href="https://cloud.google.com/vision/">Google Cloud Vision API</a>のOCR結果を利用しています。</p>

                  <br/>

                  <p v-for="(item, index) in items">
                    <a :href="item.url" target="uv">{{ item.label }}</a>
                  </p>

              </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Tabs } from "@/components";
export default {
  components: {
    Tabs
  },
  bodyClass: "profile-page",
  data: function () {
    return {
      items: [
    {
        "label": "『大日本維新史料 編年之部』・1編・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0001.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0002.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0003.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0004.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0005.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・6",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0006.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・1編・7",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/01/0007.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・2編・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/02/0001.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・2編・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/02/0002.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・2編・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/02/0003.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・2編・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/02/0004.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・2編・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/02/0005.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0001.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0002.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0003.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0004.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0005.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・6",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0006.json"
    },
    {
        "label": "『大日本維新史料 編年之部』・3編・7",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/04/03/0007.json"
    },
    {
        "label": "『大日本古文書』・伊達家文書・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/05/03/0003.json"
    },
    {
        "label": "『大日本古文書』・伊達家文書・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/05/03/0004.json"
    },
    {
        "label": "『大日本古文書』・伊達家文書・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/05/03/0005.json"
    },
    {
        "label": "『大日本古文書』・伊達家文書・8",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/05/03/0008.json"
    },
    {
        "label": "『大日本古文書』・伊達家文書・9",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/05/03/0009.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0001.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0002.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0003.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0004.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0005.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・6",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0006.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・7",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0007.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・8",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0008.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・9",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0009.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・10",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0010.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・11",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0011.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・12",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0012.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・13",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0013.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・14",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0014.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・15",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0015.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・16",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0016.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・17",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0017.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・18",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0018.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・19",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0019.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・20",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0020.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・21",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0021.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・22",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0022.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・23",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0023.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・24",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0024.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・25",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0025.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・26",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0026.json"
    },
    {
        "label": "『日本関係海外史料』・オランダ商館長日記・27",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/01/0027.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0001.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0002.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0003.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0004.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0005.json"
    },
    {
        "label": "『日本関係海外史料』・イギリス商館長日記・6",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/02/0006.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・1",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0001.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・2",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0002.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・3",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0003.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・4",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0004.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・5",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0005.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・6",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0006.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・7",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0007.json"
    },
    {
        "label": "『日本関係海外史料』・イエズス会日本書翰集・8",
        "url": "http://da.dl.itc.u-tokyo.ac.jp/uv/?manifest=https://nakamura196.github.io/hi/data/58/03/0008.json"
    }
]
    }
  },
  props: {
    header: {
      type: String,
      default: require("@/assets/img/bg7.jpg")
    }
  },
  computed: {
    headerStyle() {
      return {
        backgroundImage: `url(${this.header})`
      };
    }
  }
};
</script>

<style lang="scss" scoped>
.section {
  padding: 0;
}

.profile-tabs /deep/ {
  .md-card-tabs .md-list {
    justify-content: center;
  }

  padding-bottom: 50px;

  [class*="tab-pane-"] {
    margin-top: 3.213rem;
    padding-bottom: 50px;

    img {
      margin-bottom: 2.142rem;
    }
  }
}
</style>
