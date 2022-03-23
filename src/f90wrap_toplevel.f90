subroutine f90wrap_caps_f(y, n, stiffness, pct, res)
    implicit none
    external caps_f
    
    real(4), intent(in) :: y
    integer(4), intent(in) :: n
    integer(4), intent(in) :: stiffness
    real(4), intent(in) :: pct
    real(4), intent(out) :: res
    call caps_f(y, n, stiffness, pct, res)
end subroutine f90wrap_caps_f

