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
    page_index: 1,
    // 具体的教案
    teachfile: null,

  },
  methods: {
    change_header_title(title, page_index) {
      this.header_title = title;
      this.page_index = page_index;
      this.current_index = -1;
    },
    read_more(tf) {
      this.current_index = this.teachfiles.indexOf(tf);
      this.header_title = tf.course_name + ' ' + tf.course_id
    },
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
          this.teachfile = data;
        })
    }
  }


})