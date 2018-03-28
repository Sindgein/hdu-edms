var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    header_title: '教学档案列表',
    teach_files: [],
    teach_file: null,
    tf_index: -1,
    gradesign_files: [],
    gradesign_file: null,
    gf_index: -1,
    new_type: -1,
    page_index: 1,

  },
  methods: {
    change_header_title(title, page_index) {
      this.header_title = title;
      this.page_index = page_index;
      this.tf_index = -1;
      this.gf_index = -1;
      this.new_type = -1;
    },
    read_more(f, page_index) {
      if (page_index === 1) {
        this.tf_index = this.teach_files.indexOf(f);
        this.header_title = f.course_name + ' ' + f.course_id
      }
      else if (page_index === 2) {
        this.gf_index = this.gradesign_files.indexOf(f)
        this.header_title = f.graduation_thesis
      }
    },
    new_file(new_type) {
      this.new_type = new_type;
    }
  },
  mounted: function () {
    this.$nextTick(function () {
      $.get('/edms/api/get_teach_file_list/',
        (data) => this.teach_files = data);
      $.get('/edms/api/get_gradesign_file_list/',
        (data) => this.gradesign_files = data);
    })
  },
  watch: {
    tf_index: function () {
      $.get('/edms/api/get_teach_file_detail/' +
        this.teach_files[this.tf_index].course_id + '/',
        (data) => {
          this.teach_file = data;
        })
    },
    gf_index: function () {
      $.get('/edms/api/get_gradesign_file_detail/' +
        this.gradesign_files[this.gf_index].graduation_thesis + '/',
        (data) => {
          this.gradesign_file = data;
        })
    }
  }


})