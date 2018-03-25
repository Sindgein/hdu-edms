var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    header_title: '教学档案',
    seen: true,
    teachfiles: []

  },
  methods: {
    change_header_title(title) {
      this.header_title = title
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      $.get('/edms/api/',
        (data) => this.teachfiles = data);
    })
  }

})