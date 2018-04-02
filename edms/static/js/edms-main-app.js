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

    teachers: '',
    year: null,
    term: null,
    course_name: '',
    course_id: '',
    teaching_syllabus: null,
    file_names: [
      'teaching_syllabus',
      'teaching_plan',
      'student_score',
      'teaching_sum_up',
      'exam_paper',
      'exam_paper_answer',
      'exam_paper_analyze',
      'exam_part',
      'exam_make_up',
      'exam_make_up_answer',
      'exam_make_up_part'
    ],
    form_files: []

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
    },
    submit_teach_file() {
      var data = new FormData()
      data.append('teachers', this.teachers)
      data.append('year', this.year)
      data.append('term', this.term)
      data.append('course_name', this.course_name)
      data.append('course_id', this.course_id)
      for (i in this.form_files) {
        if (this.form_files[i].files > 0) {
          var teach_file = this.form_files[i].files[0]
          data.append(this.file_names[i], teach_file)
        }
      }
      $.ajax({
        url: '/edms/api/create_teach_file/',
        type: 'POST',
        data: data,
        cache: false,
        processData: false,
        contentType: false
      });
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
    },
    page_index: function () {

      console.log('form files ready');
      setTimeout(
        () => {
        this.form_files = [
          this.$refs.teaching_syllabus,
          this.$refs.teaching_plan,
          this.$refs.student_score,
          this.$refs.teaching_sum_up,
          this.$refs.exam_paper,
          this.$refs.exam_paper_answer,
          this.$refs.exam_paper_analyze,
          this.$refs.exam_part,
          this.$refs.exam_make_up,
          this.$refs.exam_make_up_answer,
          this.$refs.exam_make_up_part
        ]
        }, 1000)
    }

  }


})