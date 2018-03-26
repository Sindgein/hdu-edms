var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    header_title: '教学档案列表',
    seen: true,
    // 教案数组
    teachfiles: [],
    // 查看详情的数组索引
    current_index: -1,
    // 具体的教案
    teachfile: null,

  },
  methods: {
    change_header_title(title) {
      this.header_title = title
    },
    read_more(tf) {
      this.current_index = this.teachfiles.indexOf(tf)
    },
    format_file_name(url) {
      var len = url.split('/').length
      return url.split('/')[len - 1]
    },
    urldecode(str, charset, callback) {
      window._urlDecodeFn_ = callback;
      var script = document.createElement('script');
      script.id = '_urlDecodeFn_';
      var src = 'data:text/javascript;charset=' + charset + ',_urlDecodeFn_("' + str + '");'
      src += 'document.getElementById("_urlDecodeFn_").parentNode.removeChild(document.getElementById("_urlDecodeFn_"));';
      script.src = src;
      document.body.appendChild(script);
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      $.get('/edms/api/get_teachfile_list/',
        (data) => this.teachfiles = data);
    })
  },
  watch: {
    current_index: function () {
      $.get('/edms/api/get_teachfile/' + this.teachfiles[this.current_index].course_id + '/',
        (data) => {
          for (i in data) {
            data[i].filename = this.format_file_name(data[i].url, 'gbk')
          }
          this.teachfile = data;
        })
    }
  }


})